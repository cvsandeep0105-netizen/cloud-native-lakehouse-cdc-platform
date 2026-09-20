import pandas as pd
from src.bronze.config import RAW_DIR, BRONZE_DIR, EXPECTED_DATASETS

EXPECTED_COUNTS = {
    'customers': 99441,
    'geolocation': 1000163,
    'order_items': 112650,
    'order_payments': 103886,
    'order_reviews': 99224,
    'orders': 99441,
    'products': 32951,
    'sellers': 3095,
    'category_translation': 71,
}

results = []

for dataset, filename in EXPECTED_DATASETS.items():
    raw = pd.read_csv(RAW_DIR / filename)
    bronze = pd.read_parquet(BRONZE_DIR / dataset / 'part-00000.parquet')

    row_match = len(raw) == len(bronze) == EXPECTED_COUNTS[dataset]
    column_match = list(raw.columns) == list(bronze.columns)

    print(f'{dataset}: raw={len(raw)}, bronze={len(bronze)}, rows_match={row_match}, columns_match={column_match}')
    results.append(row_match and column_match)

if not all(results):
    raise RuntimeError('18-E FAIL - Raw/Bronze reconciliation failed')

print('ALL 9 DATASETS: PASS')
