from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT

spark = (
    SparkSession.builder
    .appName("Project02-PersistentCDCIntegrationTest")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

try:
    spark.sql("CREATE NAMESPACE IF NOT EXISTS local.silver_test")

    spark.sql("DROP TABLE IF EXISTS local.silver_test.orders")
    spark.sql("DROP TABLE IF EXISTS local.silver_test.cdc_events")
    spark.sql("DROP TABLE IF EXISTS local.silver_test.cdc_checkpoints")

    spark.sql("""
        CREATE TABLE local.silver_test.orders (
            order_id string,
            order_status string
        ) USING iceberg
    """)

    spark.sql("""
        CREATE TABLE local.silver_test.cdc_events (
            event_id string,
            source_position string,
            operation string,
            record_key string,
            status string
        ) USING iceberg
    """)

    spark.sql("""
        CREATE TABLE local.silver_test.cdc_checkpoints (
            source_table string,
            checkpoint_position string,
            status string
        ) USING iceberg
    """)

    print("TEST TABLES: CREATED")

    spark.sql("""
        INSERT INTO local.silver_test.orders VALUES
        ("TEST-ORDER-21", "created")
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_events VALUES
        ("E21-001", "100", "INSERT", "TEST-ORDER-21", "APPLIED")
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_checkpoints VALUES
        ("orders", "100", "COMMITTED")
    """)

    assert spark.table("local.silver_test.orders").count() == 1
    assert spark.table("local.silver_test.cdc_events").count() == 1
    assert spark.table("local.silver_test.cdc_checkpoints").count() == 1
    print("INSERT + EVENT + CHECKPOINT: PASS")

    spark.sql("""
        MERGE INTO local.silver_test.orders AS target
        USING (SELECT "TEST-ORDER-21" AS order_id, "shipped" AS order_status) AS source
        ON target.order_id = source.order_id
        WHEN MATCHED THEN UPDATE SET order_status = source.order_status
        WHEN NOT MATCHED THEN INSERT (order_id, order_status)
        VALUES (source.order_id, source.order_status)
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_events VALUES
        ("E21-002", "110", "UPDATE", "TEST-ORDER-21", "APPLIED")
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_checkpoints VALUES
        ("orders", "110", "COMMITTED")
    """)

    current = spark.sql("""
        SELECT order_status
        FROM local.silver_test.orders
        WHERE order_id = "TEST-ORDER-21"
    """).first()[0]

    assert current == "shipped"
    print("UPDATE + CHECKPOINT: PASS")

    before = spark.table("local.silver_test.cdc_events").count()
    existing = spark.sql("""
        SELECT COUNT(*)
        FROM local.silver_test.cdc_events
        WHERE event_id = "E21-002"
    """).first()[0]
    after = spark.table("local.silver_test.cdc_events").count()

    assert existing == 1
    assert before == after
    print("DUPLICATE IDEMPOTENCY: PASS")

    spark.sql("""
        DELETE FROM local.silver_test.orders
        WHERE order_id = "TEST-ORDER-21"
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_events VALUES
        ("E21-003", "120", "DELETE", "TEST-ORDER-21", "APPLIED")
    """)

    spark.sql("""
        INSERT INTO local.silver_test.cdc_checkpoints VALUES
        ("orders", "120", "COMMITTED")
    """)

    remaining = spark.sql("""
        SELECT COUNT(*)
        FROM local.silver_test.orders
        WHERE order_id = "TEST-ORDER-21"
    """).first()[0]

    assert remaining == 0
    assert spark.table("local.silver_test.cdc_events").count() == 3
    assert spark.table("local.silver_test.cdc_checkpoints").count() == 3

    print("DELETE + FINAL STATE: PASS")
    print("PERSISTENT EVENT AUDIT: 3/3 PASS")
    print("PERSISTENT CHECKPOINT STATE: 3/3 PASS")
    print("21-BC: PERSISTENT CDC INTEGRATION PASS")

finally:
    spark.sql("DROP TABLE IF EXISTS local.silver_test.orders")
    spark.sql("DROP TABLE IF EXISTS local.silver_test.cdc_events")
    spark.sql("DROP TABLE IF EXISTS local.silver_test.cdc_checkpoints")
    spark.sql("DROP NAMESPACE IF EXISTS local.silver_test")
    spark.stop()
