import os
import shutil
from pathlib import Path

from pyspark.sql import SparkSession

from src.incremental.checkpoint_store import IcebergCheckpointStore
from src.incremental.framework import (
    IncrementalEvent,
    IncrementalProcessor,
    IncrementalProcessingError,
)

project_root = Path(os.environ["PROJECT02_ROOT"])
test_root = project_root / "data" / "lake" / "incremental_test"

if test_root.exists():
    shutil.rmtree(test_root)

spark = (
    SparkSession.builder
    .appName("Project02-Area22B-Integration")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(test_root))
    .getOrCreate()
)

checkpoint_table = "local.checkpoints"
store = IcebergCheckpointStore(spark, checkpoint_table)
store.create_table()

events = [
    IncrementalEvent("B100", "area22-test", "project02", "orders", 100, "INSERT"),
    IncrementalEvent("B101", "area22-test", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("B101", "area22-test", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("B102", "area22-test", "project02", "orders", 120, "DELETE"),
    IncrementalEvent("B103", "area22-test", "project02", "orders", 130, "INSERT"),
]

processor = IncrementalProcessor()
batch1 = processor.create_batch("area22-test", "project02", "orders", 100, 120, "AREA22-B-BATCH-001")
selected1 = processor.select_events(events, batch1)

assert [event.event_id for event in selected1] == ["B100", "B101", "B102"]
assert processor.watermark(selected1) == 120

checkpoint1 = processor.next_checkpoint(batch1, selected1)
persisted1 = store.commit(checkpoint1)
assert persisted1.checkpoint_position == 120

print("22-B: FIRST INCREMENTAL BATCH: PASS")
print("22-B: CHECKPOINT PERSISTENCE: PASS")

restarted_checkpoint = store.read("area22-test", "project02", "orders")
assert restarted_checkpoint is not None
assert restarted_checkpoint.checkpoint_position == 120

restart_processor = IncrementalProcessor(restarted_checkpoint)
batch2 = restart_processor.create_batch("area22-test", "project02", "orders", 100, 130, "AREA22-B-BATCH-002")
assert batch2.start_position == 121

selected2 = restart_processor.select_events(events, batch2)
assert [event.event_id for event in selected2] == ["B103"]
assert restart_processor.watermark(selected2) == 130

print("22-B: RESTART CHECKPOINT RELOAD: PASS")
print("22-B: RESUME FROM CHECKPOINT: PASS")
print("22-B: SECOND INCREMENTAL BATCH: PASS")

before_failed_batch = store.read("area22-test", "project02", "orders")
assert before_failed_batch.checkpoint_position == 120

try:
    failing_events = [
        IncrementalEvent("FAIL-121", "area22-test", "project02", "orders", 121, "UPDATE")
    ]
    raise RuntimeError("simulated downstream processing failure")
except RuntimeError:
    pass

after_failed_batch = store.read("area22-test", "project02", "orders")
assert after_failed_batch.checkpoint_position == 120

print("22-B: FAILED-BATCH CHECKPOINT PROTECTION: PASS")

persisted2 = store.commit(
    restart_processor.next_checkpoint(batch2, selected2)
)
assert persisted2.checkpoint_position == 130

print("22-B: CHECKPOINT ADVANCEMENT AFTER SUCCESS: PASS")

try:
    store.commit(
        type(checkpoint1)(
            source_system="area22-test",
            source_schema="project02",
            source_table="orders",
            checkpoint_position=120,
        )
    )
except IncrementalProcessingError:
    pass
else:
    raise AssertionError("checkpoint regression was accepted")

print("22-B: CHECKPOINT REGRESSION PROTECTION: PASS")

final_checkpoint = store.read("area22-test", "project02", "orders")
assert final_checkpoint.checkpoint_position == 130

rows = spark.sql(f"SELECT COUNT(*) AS c FROM {checkpoint_table}").collect()[0]["c"]
assert rows == 1

print("22-B: FINAL PERSISTED CHECKPOINT: 130")
print("22-B: SINGLE ACTIVE CHECKPOINT STATE: PASS")

spark.stop()

if test_root.exists():
    shutil.rmtree(test_root)

assert not test_root.exists()
print("22-B: TEMPORARY TEST STATE CLEANUP: PASS")
print("22-B: INCREMENTAL BATCH/CHECKPOINT INTEGRATION: PASS")
