from pyspark.sql import SparkSession

from src.silver.config import ICEBERG_ROOT, DATASETS

spark = (
    SparkSession.builder
    .appName("Project02-SilverCDCMetadataValidation")
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

required = {
    "cdc_event_id",
    "cdc_operation",
    "cdc_source_position",
    "cdc_event_timestamp",
    "cdc_processed_at",
    "cdc_record_version"
}

try:
    passed = 0

    for dataset in DATASETS:
        columns = set(
            spark.table(f"local.silver.{dataset}").columns
        )

        missing = required - columns

        print(
            f"{dataset}: cdc_metadata_missing={sorted(missing)}"
        )

        if missing:
            raise AssertionError(
                f"CDC metadata validation failed: {dataset}"
            )

        passed += 1

    print(f"21-BJ: CDC METADATA VALIDATION {passed}/{len(DATASETS)} PASS")

finally:
    spark.stop()
