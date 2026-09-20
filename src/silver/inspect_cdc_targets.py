from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT, DATASETS
from src.silver.record_identity import RECORD_IDENTITY

spark = (
    SparkSession.builder
    .appName("Project02-SilverCDCTargetInspection")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

try:
    for dataset in DATASETS:
        df = spark.table(f"local.silver.{dataset}")
        required = RECORD_IDENTITY[dataset]
        missing = [c for c in required if c not in df.columns]
        print(f"{dataset}: rows={df.count()}, identity={required}, missing={missing}")
        if missing:
            raise AssertionError(f"Identity missing for {dataset}: {missing}")
    print("21-BG: ALL 9 SILVER CDC TARGETS READY")
finally:
    spark.stop()
