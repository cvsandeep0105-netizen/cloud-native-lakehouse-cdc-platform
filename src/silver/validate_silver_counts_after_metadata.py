from pyspark.sql import SparkSession

from src.silver.config import ICEBERG_ROOT

EXPECTED = {
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

spark = (
    SparkSession.builder
    .appName("Project02-SilverCountValidation")
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

try:
    passed = 0

    for dataset, expected in EXPECTED.items():
        actual = spark.table(
            f"local.silver.{dataset}"
        ).count()

        print(
            f"{dataset}: expected={expected}, actual={actual}"
        )

        if actual != expected:
            raise AssertionError(
                f"Silver count changed for {dataset}"
            )

        passed += 1

    print(f"21-BK: SILVER BUSINESS COUNTS {passed}/9 PRESERVED")

finally:
    spark.stop()
