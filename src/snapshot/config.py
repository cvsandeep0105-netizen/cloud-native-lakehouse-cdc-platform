from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = PROJECT_ROOT / 'data' / 'raw' / 'olist' / 'extracted'

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'
DB_SCHEMA = 'project02'

LOAD_ORDER = [
    'customers',
    'products',
    'sellers',
    'category_translation',
    'orders',
    'order_items',
    'order_payments',
    'order_reviews',
    'geolocation',
]
DB_USER = 'postgres'
