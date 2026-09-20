from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT

spark = (
    SparkSession.builder
    .appName('Project02-SilverMetadataInspection')
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
    .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
    .config('spark.sql.catalog.local.type', 'hadoop')
    .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

try:
    table = spark.table('local.silver.orders')
    print('COLUMNS:', table.columns)
    print('SCHEMA:')
    table.printSchema()
    print('SNAPSHOTS:')
    spark.sql('SELECT * FROM local.silver.orders.snapshots').show(truncate=False)
finally:
    spark.stop()
