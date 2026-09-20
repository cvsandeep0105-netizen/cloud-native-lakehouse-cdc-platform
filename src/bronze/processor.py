from pathlib import Path

import pandas as pd

from .config import RAW_DIR, BRONZE_DIR, EXPECTED_DATASETS


TIMESTAMP_COLUMNS = {
    'orders': [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
    ],
    'order_items': ['shipping_limit_date'],
    'order_reviews': ['review_creation_date', 'review_answer_timestamp'],
}

INTEGER_COLUMNS = {
    'products': [
        'product_name_lenght',
        'product_description_lenght',
        'product_photos_qty',
        'product_weight_g',
        'product_length_cm',
        'product_height_cm',
        'product_width_cm',
    ],
}


def source_path(dataset: str) -> Path:
    return RAW_DIR / EXPECTED_DATASETS[dataset]


def bronze_path(dataset: str) -> Path:
    return BRONZE_DIR / dataset


def prepare_dataframe(dataset: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()

    for column in TIMESTAMP_COLUMNS.get(dataset, []):
        result[column] = pd.to_datetime(result[column], errors='raise').astype('datetime64[ms]')

    for column in INTEGER_COLUMNS.get(dataset, []):
        result[column] = result[column].astype('Int64')

    return result


def validate_source_inventory() -> None:
    if not RAW_DIR.exists():
        raise RuntimeError(f'Raw directory does not exist: {RAW_DIR}')

    actual = {file.name for file in RAW_DIR.glob('*.csv')}
    expected = set(EXPECTED_DATASETS.values())

    if actual != expected:
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        raise RuntimeError(
            f'Raw inventory mismatch; missing={missing}; unexpected={unexpected}'
        )


def process_dataset(dataset: str) -> int:
    dataframe = pd.read_csv(source_path(dataset))
    dataframe = prepare_dataframe(dataset, dataframe)

    output_dir = bronze_path(dataset)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / 'part-00000.parquet'
    dataframe.to_parquet(output_file, index=False)

    return len(dataframe)


def build_bronze() -> dict[str, int]:
    validate_source_inventory()
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)

    counts = {}

    for dataset in EXPECTED_DATASETS:
        counts[dataset] = process_dataset(dataset)

    return counts
