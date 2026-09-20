from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT

spark = (
    SparkSession.builder
    .appName('Project02-SilverCDCControlTables')
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
    .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
    .config('spark.sql.catalog.local.type', 'hadoop')
    .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

try:
    spark.sql('CREATE NAMESPACE IF NOT EXISTS local.silver')

    spark.sql('''
    CREATE TABLE IF NOT EXISTS local.silver.silver_cdc_events (
        event_id string,
        source_system string,
        source_schema string,
        source_table string,
        transaction_id string,
        source_position string,
        event_sequence string,
        operation string,
        record_key string,
        event_timestamp timestamp,
        processed_at timestamp,
        status string
    ) USING iceberg
    ''')

    spark.sql('''
    CREATE TABLE IF NOT EXISTS local.silver.silver_cdc_checkpoints (
        source_system string,
        source_schema string,
        source_table string,
        checkpoint_position string,
        updated_at timestamp,
        status string
    ) USING iceberg
    ''')

    print('CDC CONTROL TABLES: CREATED/EXISTING')
    print('silver_cdc_events:', spark.table('local.silver.silver_cdc_events').count())
    print('silver_cdc_checkpoints:', spark.table('local.silver.silver_cdc_checkpoints').count())
finally:
    spark.stop()
