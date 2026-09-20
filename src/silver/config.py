from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ICEBERG_ROOT = PROJECT_ROOT / 'data' / 'lake' / 'iceberg' / 'olist' / 'olist'
SILVER_ROOT = PROJECT_ROOT / 'data' / 'lake' / 'silver' / 'olist'

DATASETS = [
    'customers',
    'geolocation',
    'order_items',
    'order_payments',
    'order_reviews',
    'orders',
    'products',
    'sellers',
    'category_translation',
]

CDC_OPERATIONS = {'INSERT', 'UPDATE', 'DELETE'}
