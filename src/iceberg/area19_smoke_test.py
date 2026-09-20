from pyspark.sql import SparkSession

warehouse = r'C:\p02_area19_test\warehouse'

spark = (
    SparkSession.builder
    .appName('Project02-Area19-Iceberg-SmokeTest')
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
    .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
    .config('spark.sql.catalog.local.type', 'hadoop')
    .config('spark.sql.catalog.local.warehouse', warehouse)
    .getOrCreate()
)

spark.sql('CREATE NAMESPACE IF NOT EXISTS local.area19_test')
spark.sql('DROP TABLE IF EXISTS local.area19_test.smoke')
spark.sql('CREATE TABLE local.area19_test.smoke (id BIGINT, value STRING) USING iceberg')
spark.sql("INSERT INTO local.area19_test.smoke VALUES (1, 'area19'), (2, 'iceberg')")

rows = spark.sql('SELECT * FROM local.area19_test.smoke ORDER BY id').collect()
assert len(rows) == 2
assert rows[0]['id'] == 1
assert rows[1]['id'] == 2

snapshots = spark.sql('SELECT * FROM local.area19_test.smoke.snapshots').collect()
assert len(snapshots) >= 1

print('ICEBERG TABLE: PASS')
print('ROWS WRITTEN:', len(rows))
print('SNAPSHOTS:', len(snapshots))
print('CURRENT SNAPSHOT ID:', snapshots[-1]['snapshot_id'])

spark.sql('DROP TABLE local.area19_test.smoke')
spark.stop()
print('ICEBERG RUNTIME: PASS')
