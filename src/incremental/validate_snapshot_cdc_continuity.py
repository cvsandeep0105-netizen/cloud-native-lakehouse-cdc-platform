import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession

from src.incremental.framework import IncrementalEvent, IncrementalProcessor
from src.incremental.checkpoint_store import IcebergCheckpointStore

project_root = Path(os.environ["PROJECT02_ROOT"])
test_root = project_root / "data" / "lake" / "incremental_continuity_test"

if test_root.exists():
    shutil.rmtree(test_root)

spark = (
    SparkSession.builder
    .appName("Project02-Area22C-SnapshotCDCContinuity")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(project_root / "data" / "lake" / "iceberg" / "olist"))
    .getOrCreate()
)

datasets = {
    "customers": 99441,
    "geolocation": 1000163,
    "order_items": 112650,
    "order_payments": 103886,
    "order_reviews": 99224,
    "orders": 99441,
    "products": 32951,
    "sellers": 3095,
    "category_translation": 71,
}

print("===== 22-C SNAPSHOT BASELINE =====")

for dataset, expected in datasets.items():
    snapshot_table = f"local.olist.{dataset}"
    silver_table = f"local.silver.{dataset}"

    snapshot_count = spark.sql(f"SELECT COUNT(*) AS c FROM {snapshot_table}").collect()[0]["c"]
    silver_count = spark.sql(f"SELECT COUNT(*) AS c FROM {silver_table}").collect()[0]["c"]

    assert snapshot_count == expected, f"{dataset}: snapshot count {snapshot_count} != {expected}"
    assert silver_count == expected, f"{dataset}: silver count {silver_count} != {expected}"
    assert snapshot_count == silver_count, f"{dataset}: snapshot/silver mismatch"

    print(f"SNAPSHOT/SILVER {dataset}: PASS ({snapshot_count})")

print("22-C: ALL 9 SNAPSHOT BASELINES: PASS")

orders_snapshot = spark.sql("SELECT * FROM local.olist.orders")
orders_silver = spark.sql("SELECT * FROM local.silver.orders")

assert orders_snapshot.count() == orders_silver.count() == 99441
snapshot_columns = set(orders_snapshot.columns)
silver_business_columns = set(orders_snapshot.columns).issubset(set(orders_silver.columns))
assert silver_business_columns

print("22-C: SNAPSHOT BUSINESS-COLUMN CONTINUITY: PASS")

processor = IncrementalProcessor()

snapshot_checkpoint_position = 0
events = [
    IncrementalEvent("C100", "area22-continuity", "project02", "orders", 100, "INSERT"),
    IncrementalEvent("C101", "area22-continuity", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("C101", "area22-continuity", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("C102", "area22-continuity", "project02", "orders", 120, "DELETE"),
    IncrementalEvent("C103", "area22-continuity", "project02", "orders", 130, "INSERT"),
]

batch1 = processor.create_batch(
    "area22-continuity", "project02", "orders",
    snapshot_checkpoint_position + 1, 120, "AREA22-C-BATCH-001"
)

assert batch1.start_position == 1
assert batch1.end_position == 120

selected1 = processor.select_events(events, batch1)
assert [event.event_id for event in selected1] == ["C100", "C101", "C102"]
assert processor.watermark(selected1) == 120

checkpoint1 = processor.next_checkpoint(batch1, selected1)
assert checkpoint1.checkpoint_position == 120

print("22-C: SNAPSHOT -> CDC START BOUNDARY: PASS")
print("22-C: FIRST CDC WINDOW: PASS")
print("22-C: CDC WATERMARK 120: PASS")

restart_processor = IncrementalProcessor(checkpoint1)
batch2 = restart_processor.create_batch(
    "area22-continuity", "project02", "orders",
    1, 130, "AREA22-C-BATCH-002"
)

assert batch2.start_position == 121

selected2 = restart_processor.select_events(events, batch2)
assert [event.event_id for event in selected2] == ["C103"]
assert restart_processor.watermark(selected2) == 130

checkpoint2 = restart_processor.next_checkpoint(batch2, selected2)
assert checkpoint2.checkpoint_position == 130

print("22-C: CDC RESTART FROM CHECKPOINT 120: PASS")
print("22-C: SECOND CDC WINDOW: PASS")
print("22-C: CDC WATERMARK 130: PASS")

store = IcebergCheckpointStore(spark, "local.continuity_checkpoints")
store.create_table()

persisted1 = store.commit(checkpoint1)
assert persisted1.checkpoint_position == 120

persisted2 = store.commit(checkpoint2)
assert persisted2.checkpoint_position == 130

reloaded = store.read("area22-continuity", "project02", "orders")
assert reloaded is not None
assert reloaded.checkpoint_position == 130

print("22-C: PERSISTED CDC CHECKPOINT: PASS")
print("22-C: RELOADED FINAL CHECKPOINT 130: PASS")

final_snapshot_count = spark.sql("SELECT COUNT(*) AS c FROM local.olist.orders").collect()[0]["c"]
final_silver_count = spark.sql("SELECT COUNT(*) AS c FROM local.silver.orders").collect()[0]["c"]
assert final_snapshot_count == 99441
assert final_silver_count == 99441

print("22-C: PROJECT SNAPSHOT UNCHANGED: PASS")
print("22-C: PROJECT SILVER UNCHANGED: PASS")

spark.sql("DROP TABLE IF EXISTS local.continuity_checkpoints")
spark.stop()

if test_root.exists():
    shutil.rmtree(test_root)

print("22-C: TEMPORARY STATE CLEANUP: PASS")
print("22-C: SNAPSHOT + CDC CONTINUITY VALIDATION: PASS")
