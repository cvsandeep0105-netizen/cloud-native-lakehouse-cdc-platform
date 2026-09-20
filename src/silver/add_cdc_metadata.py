from pyspark.sql import SparkSession

from src.silver.config import ICEBERG_ROOT, DATASETS

spark = (
    SparkSession.builder
    .appName("Project02-SilverCDCMetadata")
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

CDC_COLUMNS = {
    "cdc_event_id": "string",
    "cdc_operation": "string",
    "cdc_source_position": "string",
    "cdc_event_timestamp": "timestamp",
    "cdc_processed_at": "timestamp",
    "cdc_record_version": "long"
}

try:
    for dataset in DATASETS:
        table = f"local.silver.{dataset}"
        existing = set(spark.table(table).columns)

        missing = [
            (name, dtype)
            for name, dtype in CDC_COLUMNS.items()
            if name not in existing
        ]

        for name, dtype in missing:
            spark.sql(
                f"ALTER TABLE {table} ADD COLUMN {name} {dtype}"
            )

        final_columns = set(spark.table(table).columns)

        if not set(CDC_COLUMNS).issubset(final_columns):
            raise AssertionError(
                f"CDC metadata missing after alteration: {dataset}"
            )

        print(
            f"{dataset}: metadata_added={len(missing)}, "
            f"cdc_columns=6"
        )

    print("21-BI: CDC METADATA ADDED/VERIFIED 9/9")

finally:
    spark.stop()
