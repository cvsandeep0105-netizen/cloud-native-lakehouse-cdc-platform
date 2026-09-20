from pathlib import Path
from typing import Iterable

from pyspark.sql import DataFrame, SparkSession

from src.silver.config import ICEBERG_ROOT, SILVER_ROOT, DATASETS

def build_spark() -> SparkSession:
    return (
        SparkSession.builder
        .appName('Project02-SilverCDC')
        .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions')
        .config('spark.sql.catalog.local', 'org.apache.iceberg.spark.SparkCatalog')
        .config('spark.sql.catalog.local.type', 'hadoop')
        .config('spark.sql.catalog.local.warehouse', str(ICEBERG_ROOT.parent))
        .getOrCreate()
    )

def read_iceberg_table(spark: SparkSession, dataset: str) -> DataFrame:
    if dataset not in DATASETS:
        raise ValueError(f'Unsupported dataset: {dataset}')
    return spark.table(f'local.olist.{dataset}')

def validate_source_state(df: DataFrame) -> None:
    if df.columns is None or len(df.columns) == 0:
        raise ValueError('Silver input must contain at least one column')

def ensure_silver_root() -> Path:
    SILVER_ROOT.mkdir(parents=True, exist_ok=True)
    return SILVER_ROOT

def validate_dataset_inventory(datasets: Iterable[str]) -> None:
    actual = set(datasets)
    expected = set(DATASETS)
    if actual != expected:
        raise ValueError(f'Dataset inventory mismatch: expected={sorted(expected)}, actual={sorted(actual)}')
