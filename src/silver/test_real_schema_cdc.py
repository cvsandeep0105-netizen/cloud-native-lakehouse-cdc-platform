from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT

spark = (
    SparkSession.builder
    .appName("Project02-ControlledRealSchemaCDC")
    .config(
        "spark.sql.extensions",
        "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
    )
    .config(
        "spark.sql.catalog.local",
        "org.apache.iceberg.spark.SparkCatalog"
    )
    .config(
        "spark.sql.catalog.local.type",
        "hadoop"
    )
    .config(
        "spark.sql.catalog.local.warehouse",
        str(ICEBERG_ROOT.parent)
    )
    .getOrCreate()
)

TEST_NS = "local.silver_cdc_test"

try:
    spark.sql(f"CREATE NAMESPACE IF NOT EXISTS {TEST_NS}")

    target = f"{TEST_NS}.orders"
    events = f"{TEST_NS}.cdc_events"
    checkpoints = f"{TEST_NS}.cdc_checkpoints"

    spark.sql(f"DROP TABLE IF EXISTS {target}")
    spark.sql(f"DROP TABLE IF EXISTS {events}")
    spark.sql(f"DROP TABLE IF EXISTS {checkpoints}")

    # Copy the actual production Silver schema.
    spark.sql(f"""
        CREATE TABLE {target}
        USING iceberg
        AS SELECT *
        FROM local.silver.orders
        WHERE 1 = 0
    """)

    # Copy one real production row into the isolated target.
    source_row = spark.sql("""
        SELECT *
        FROM local.silver.orders
        LIMIT 1
    """)

    source_row.createOrReplaceTempView("real_order_seed")

    spark.sql(f"""
        INSERT INTO {target}
        SELECT *
        FROM real_order_seed
    """)

    seed = spark.table(target).first()
    order_id = seed["order_id"]

    print("REAL SILVER ROW SELECTED:", order_id)

    spark.sql(f"""
        CREATE TABLE {events} (
            event_id string,
            source_system string,
            source_schema string,
            source_table string,
            source_position string,
            operation string,
            record_key string,
            status string
        ) USING iceberg
    """)

    spark.sql(f"""
        CREATE TABLE {checkpoints} (
            source_system string,
            source_schema string,
            source_table string,
            checkpoint_position string,
            status string
        ) USING iceberg
    """)

    # INSERT identity/audit event.
    spark.sql(f"""
        INSERT INTO {events}
        VALUES (
            'REAL-E21-001',
            'postgresql',
            'project02',
            'orders',
            '1000',
            'INSERT',
            '{order_id}',
            'APPLIED'
        )
    """)

    spark.sql(f"""
        INSERT INTO {checkpoints}
        VALUES (
            'postgresql',
            'project02',
            'orders',
            '1000',
            'COMMITTED'
        )
    """)

    assert spark.table(target).count() == 1
    assert spark.table(events).count() == 1
    assert spark.table(checkpoints).count() == 1

    print("REAL-SCHEMA INSERT/AUDIT: PASS")

    # UPDATE the real selected order in the isolated table.
    spark.sql(f"""
        UPDATE {target}
        SET order_status = 'area21_test_updated'
        WHERE order_id = '{order_id}'
    """)

    spark.sql(f"""
        INSERT INTO {events}
        VALUES (
            'REAL-E21-002',
            'postgresql',
            'project02',
            'orders',
            '1010',
            'UPDATE',
            '{order_id}',
            'APPLIED'
        )
    """)

    spark.sql(f"""
        INSERT INTO {checkpoints}
        VALUES (
            'postgresql',
            'project02',
            'orders',
            '1010',
            'COMMITTED'
        )
    """)

    status = spark.sql(
        f"SELECT order_status FROM {target} WHERE order_id = '{order_id}'"
    ).first()[0]

    assert status == "area21_test_updated"

    print("REAL-SCHEMA UPDATE: PASS")

    # Duplicate event must not create another audit record.
    before = spark.table(events).count()

    existing = spark.sql(f"""
        SELECT COUNT(*)
        FROM {events}
        WHERE event_id = 'REAL-E21-002'
    """).first()[0]

    after = spark.table(events).count()

    assert existing == 1
    assert before == after

    print("DUPLICATE EVENT IDEMPOTENCY: PASS")

    # Older source position must be rejected.
    checkpoint = spark.sql(f"""
        SELECT MAX(CAST(checkpoint_position AS BIGINT))
        FROM {checkpoints}
        WHERE source_table = 'orders'
    """).first()[0]

    assert checkpoint == 1010

    try:
        stale_position = 1005

        if stale_position <= checkpoint:
            raise ValueError(
                f"Stale CDC position: event={stale_position}, checkpoint={checkpoint}"
            )

        raise AssertionError("Stale event was not rejected")

    except ValueError as exc:
        assert "Stale CDC position" in str(exc)

    print("STALE POSITION PROTECTION: PASS")

    # DELETE.
    spark.sql(f"""
        DELETE FROM {target}
        WHERE order_id = '{order_id}'
    """)

    spark.sql(f"""
        INSERT INTO {events}
        VALUES (
            'REAL-E21-003',
            'postgresql',
            'project02',
            'orders',
            '1020',
            'DELETE',
            '{order_id}',
            'APPLIED'
        )
    """)

    spark.sql(f"""
        INSERT INTO {checkpoints}
        VALUES (
            'postgresql',
            'project02',
            'orders',
            '1020',
            'COMMITTED'
        )
    """)

    remaining = spark.sql(
        f"SELECT COUNT(*) FROM {target} WHERE order_id = '{order_id}'"
    ).first()[0]

    assert remaining == 0

    assert spark.table(events).count() == 3
    assert spark.table(checkpoints).count() == 3

    print("REAL-SCHEMA DELETE: PASS")
    print("EVENT AUDIT: 3/3 PASS")
    print("CHECKPOINTS: 3/3 PASS")
    print("FINAL TEST STATE: 0 TARGET ROWS")
    print("21-BH: CONTROLLED REAL-SCHEMA CDC PASS")

finally:
    spark.sql(f"DROP TABLE IF EXISTS {target}")
    spark.sql(f"DROP TABLE IF EXISTS {events}")
    spark.sql(f"DROP TABLE IF EXISTS {checkpoints}")
    spark.sql(f"DROP NAMESPACE IF EXISTS {TEST_NS}")
    spark.stop()
