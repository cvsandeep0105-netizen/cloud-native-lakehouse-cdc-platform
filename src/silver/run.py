from src.silver.processor import build_spark, read_iceberg_table, validate_source_state, ensure_silver_root
from src.silver.config import DATASETS

def main() -> None:
    spark = build_spark()
    try:
        ensure_silver_root()
        print('SILVER ROOT:', ensure_silver_root())
        for dataset in DATASETS:
            df = read_iceberg_table(spark, dataset)
            validate_source_state(df)
            print(f'{dataset}: INPUT READY ({len(df.columns)} columns)')
        print(f'SILVER INPUT DATASETS READY: {len(DATASETS)}/{len(DATASETS)}')
    finally:
        spark.stop()

if __name__ == '__main__':
    main()
