from pathlib import Path
import json
from pyspark.sql import SparkSession

PROJECT_ROOT = Path(r'C:\Users\sandeep\Desktop\Cloud-Native Lakehouse, CDC & AI-Ready Data')
BRONZE_ROOT = PROJECT_ROOT / 'data' / 'lake' / 'bronze' / 'olist'
ICEBERG_ROOT = PROJECT_ROOT / 'data' / 'lake' / 'iceberg' / 'olist'

DATASETS = [
    'customers',
    'geolocation',
    'order_items',
    'order_payments',
    'order_reviews',
    'orders',
    'products',
    'sellers',
    'category_translation',
]

spark = (
    SparkSession.builder
    .appName('Project02-Area19-Iceberg-Foundation')
    .master('local[*]')
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
    .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
    .config('spark.sql.catalog.local.type', 'hadoop')
    .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT))
    .getOrCreate()
)

spark.sql('CREATE NAMESPACE IF NOT EXISTS local.olist')

results = []

for dataset in DATASETS:
    bronze_path = BRONZE_ROOT / dataset
    table = f'local.olist.{dataset}'

    bronze_df = spark.read.parquet(str(bronze_path))
    bronze_count = bronze_df.count()

    spark.sql(f'DROP TABLE IF EXISTS {table}')
    bronze_df.createOrReplaceTempView('bronze_source')
    spark.sql(f'CREATE TABLE {table} USING iceberg AS SELECT * FROM bronze_source')

    iceberg_count = spark.sql(f'SELECT COUNT(*) AS c FROM {table}').first()['c']
    snapshots = spark.sql(f'SELECT * FROM {table}.snapshots').count()

    columns = spark.table(table).columns
    bronze_columns = bronze_df.columns

    if iceberg_count != bronze_count:
        raise RuntimeError(f'{dataset}: row count mismatch Bronze={bronze_count} Iceberg={iceberg_count}')

    if columns != bronze_columns:
        raise RuntimeError(f'{dataset}: column mismatch')

    if snapshots < 1:
        raise RuntimeError(f'{dataset}: no Iceberg snapshot created')

    print(f'ICEBERG DATASET PASS: {dataset} | rows={iceberg_count} | snapshots={snapshots}')

    results.append({
        'dataset': dataset,
        'bronze_rows': bronze_count,
        'iceberg_rows': iceberg_count,
        'snapshots': snapshots,
        'columns': len(columns)
    })

print('')
print('===== ICEBERG FOUNDATION VALIDATION =====')
print(json.dumps(results, indent=2))
print('DATASETS PASSED:', len(results))

spark.stop()
print('ICEBERG FOUNDATION: PASS')
