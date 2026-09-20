from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Project02-SilverSchemaInspection")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", r"C:\Users\sandeep\Desktop\Cloud-Native Lakehouse, CDC & AI-Ready Data\data\lake\iceberg\olist")
    .getOrCreate()
)

tables = [
    "customers", "orders", "products", "order_items",
    "order_payments", "order_reviews", "sellers",
    "geolocation", "category_translation"
]

try:
    for table in tables:
        print(f"===== {table} =====")
        spark.table(f"local.silver.{table}").printSchema()
finally:
    spark.stop()
