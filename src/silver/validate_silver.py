from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT, DATASETS

def build_spark() -> SparkSession:
    return (
        SparkSession.builder
        .appName('Project02-SilverValidation')
        .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
        .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
        .config('spark.sql.catalog.local.type', 'hadoop')
        .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT.parent))
        .getOrCreate()
    )

def main() -> None:
    spark = build_spark()
    try:
        passed = 0
        for dataset in DATASETS:
            source = spark.table(f'local.olist.{dataset}')
            silver = spark.table(f'local.silver.{dataset}')
            source_count = source.count()
            silver_count = silver.count()
            columns_match = source.columns == silver.columns
            counts_match = source_count == silver_count
            print(f'{dataset}: source={source_count}, silver={silver_count}, columns_match={columns_match}')
            if not counts_match or not columns_match:
                raise AssertionError(f'Silver reconciliation failed for {dataset}')
            passed += 1
        print(f'SILVER RECONCILIATION: {passed}/{len(DATASETS)} PASS')
    finally:
        spark.stop()

if __name__ == '__main__':
    main()
