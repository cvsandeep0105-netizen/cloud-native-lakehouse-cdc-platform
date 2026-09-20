from pyspark.sql import SparkSession
from src.silver.config import ICEBERG_ROOT, DATASETS
from src.silver.record_identity import RECORD_IDENTITY

spark = (
    SparkSession.builder
    .appName("Project02-RecordIdentityValidation")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

try:
    failures = []
    for dataset in DATASETS:
        columns = spark.table(f"local.silver.{dataset}").columns
        required = RECORD_IDENTITY[dataset]
        missing = [c for c in required if c not in columns]
        print(f"{dataset}: required={required}, missing={missing}")
        if missing:
            failures.append((dataset, missing))

    if failures:
        print("21-AW: IDENTITY/SCHEMA RECONCILIATION REQUIRES DESIGN FIX")
        for dataset, missing in failures:
            print(f"  {dataset}: missing {missing}")
        raise SystemExit(2)

    print("21-AW: IDENTITY/SCHEMA RECONCILIATION PASS")
finally:
    spark.stop()
