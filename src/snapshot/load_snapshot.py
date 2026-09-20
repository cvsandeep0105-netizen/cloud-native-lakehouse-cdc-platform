from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from .config import DB_USER, DB_HOST, DB_PORT, DB_NAME, DB_SCHEMA, SOURCE_DIR, LOAD_ORDER

TABLE_FILES = {
    'customers': 'olist_customers_dataset.csv',
    'products': 'olist_products_dataset.csv',
    'sellers': 'olist_sellers_dataset.csv',
    'category_translation': 'product_category_name_translation.csv',
    'orders': 'olist_orders_dataset.csv',
    'order_items': 'olist_order_items_dataset.csv',
    'order_payments': 'olist_order_payments_dataset.csv',
    'order_reviews': 'olist_order_reviews_dataset.csv',
    'geolocation': 'olist_geolocation_dataset.csv',
}

def build_engine():
    return create_engine(f'postgresql+psycopg://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}', future=True)

def source_path(table_name: str) -> Path:
    return SOURCE_DIR / TABLE_FILES[table_name]

def load_source_dataframe(table_name: str) -> pd.DataFrame:
    return pd.read_csv(source_path(table_name))


def target_table_row_count(engine, table_name: str) -> int:
    with engine.connect() as connection:
        result = connection.exec_driver_sql(f'SELECT COUNT(*) FROM {DB_SCHEMA}.{table_name}')
        return int(result.scalar_one())



def validate_empty_target(engine) -> None:
    populated_tables = []
    for table_name in LOAD_ORDER:
        row_count = target_table_row_count(engine, table_name)
        if row_count > 0:
            populated_tables.append(f'{table_name}={row_count}')
    if populated_tables:
        raise RuntimeError('Snapshot target is not empty: ' + ', '.join(populated_tables))



def missing_target_tables(engine) -> list[str]:
    with engine.connect() as connection:
        result = connection.exec_driver_sql(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = %s AND table_name = ANY(%s)" ,
            (DB_SCHEMA, LOAD_ORDER),
        )
        existing_tables = {row[0] for row in result}
    return [table_name for table_name in LOAD_ORDER if table_name not in existing_tables]



def target_state(engine) -> str:
    missing = missing_target_tables(engine)
    if missing:
        return 'MISSING_TABLES'
    populated = [table_name for table_name in LOAD_ORDER if target_table_row_count(engine, table_name) > 0]
    if populated:
        return 'POPULATED'
    return 'EMPTY'



GENERATED_COLUMNS = {'geolocation': {'geolocation_id'}, 'order_reviews': {'order_review_key'}}

def validate_source_target_columns(engine) -> None:
    from sqlalchemy import inspect
    inspector = inspect(engine)
    for table_name in LOAD_ORDER:
        target_columns = [column['name'] for column in inspector.get_columns(table_name, schema=DB_SCHEMA) if column['name'] not in GENERATED_COLUMNS.get(table_name, set())]
        source_columns = list(load_source_dataframe(table_name).columns)
        if source_columns != target_columns:
            raise ValueError(f'Column mismatch for {table_name}: source={source_columns}; target={target_columns}')



def prepare_dataframe(table_name: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()
    timestamp_columns = {'orders': ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'], 'order_items': ['shipping_limit_date'], 'order_reviews': ['review_creation_date', 'review_answer_timestamp']}
    for column in timestamp_columns.get(table_name, []):
        result[column] = pd.to_datetime(result[column], errors='raise')
    integer_columns = {'products': ['product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']}
    for column in integer_columns.get(table_name, []):
        result[column] = result[column].astype('Int64')
    return result



def write_snapshot_table(engine, table_name: str, dataframe: pd.DataFrame) -> None:
    state = target_state(engine)
    if state == 'POPULATED':
        raise RuntimeError('Snapshot target is already populated; refusing to write.')
    if state == 'MISSING_TABLES':
        raise RuntimeError('Snapshot target schema is incomplete; refusing to write.')
    dataframe.to_sql(table_name, engine, schema=DB_SCHEMA, if_exists='append', index=False, method='multi', chunksize=1000)



def write_full_snapshot(engine) -> None:
    state = target_state(engine)
    if state == 'POPULATED':
        raise RuntimeError('Snapshot target is already populated; refusing to start full snapshot.')
    if state == 'MISSING_TABLES':
        raise RuntimeError('Snapshot target schema is incomplete; refusing to start full snapshot.')
    if state != 'EMPTY':
        raise RuntimeError(f'Unexpected snapshot target state: {state}')
    for table_name in LOAD_ORDER:
        dataframe = prepare_dataframe(table_name, load_source_dataframe(table_name))
        dataframe.to_sql(table_name, engine, schema=DB_SCHEMA, if_exists='append', index=False, method='multi', chunksize=1000)
