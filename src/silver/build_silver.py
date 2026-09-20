from pathlib import Path
from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT, SILVER_ROOT, DATASETS

def build_spark() -> SparkSession:
    return (
        SparkSession.builder
        .appName('Project02-SilverBuild')
        .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
        .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
        .config('spark.sql.catalog.local.type', 'hadoop')
        .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT.parent))
        .getOrCreate()
    )

def main() -> None:
    spark = build_spark()
    try:
        SILVER_ROOT.mkdir(parents=True, exist_ok=True)
        print('SILVER ROOT:', SILVER_ROOT)
        spark.sql('CREATE NAMESPACE IF NOT EXISTS local.silver')

        passed = 0
        for dataset in DATASETS:
            source = spark.table(f'local.olist.{dataset}')
            target = f'local.silver.{dataset}'
            spark.sql(f'DROP TABLE IF EXISTS {target}')
            source.createOrReplaceTempView('silver_source')
            spark.sql(f'CREATE TABLE {target} USING iceberg AS SELECT * FROM silver_source')
            count = spark.table(target).count()
            print(f'{dataset}: {count} rows')
            passed += 1

        print(f'SILVER TABLES CREATED: {passed}/{len(DATASETS)}')
    finally:
        spark.stop()

if __name__ == '__main__':
    main()
