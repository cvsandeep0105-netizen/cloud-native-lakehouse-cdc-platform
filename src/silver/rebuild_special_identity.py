import psycopg
from pyspark.sql import SparkSession

from src.silver.config import ICEBERG_ROOT

spark = (
    SparkSession.builder
    .appName("Project02-SilverSpecialIdentity")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", str(ICEBERG_ROOT.parent))
    .getOrCreate()
)

conn = psycopg.connect(
    "host=localhost port=5432 dbname=postgres user=postgres"
)

try:
    spark.sql("CREATE NAMESPACE IF NOT EXISTS local.silver")

    for table, key in [
        ("geolocation", "geolocation_id"),
        ("order_reviews", "order_review_key")
    ]:
        print(f"===== REBUILD {table} =====")

        query = f"""
            SELECT *
            FROM project02.{table}
            ORDER BY {key}
        """

        pdf = None

        import pandas as pd
        pdf = pd.read_sql_query(query, conn)

        if len(pdf) == 0:
            raise RuntimeError(f"{table} operational source is empty")

        df = spark.createDataFrame(pdf)

        target = f"local.silver.{table}"
        spark.sql(f"DROP TABLE IF EXISTS {target}")

        df.createOrReplaceTempView("special_identity_source")

        spark.sql(
            f"""
            CREATE TABLE {target}
            USING iceberg
            AS SELECT * FROM special_identity_source
            """
        )

        actual = spark.table(target)

        count = actual.count()
        distinct_keys = actual.select(key).distinct().count()

        print(f"{table}: rows={count}")
        print(f"{table}: distinct_{key}={distinct_keys}")

        if count != len(pdf):
            raise AssertionError(f"{table}: row-count mismatch")

        if distinct_keys != count:
            raise AssertionError(f"{table}: technical key is not unique")

        print(f"{table}: SPECIAL IDENTITY PASS")

    print("SPECIAL IDENTITY SILVER REBUILD: PASS")

finally:
    conn.close()
    spark.stop()
