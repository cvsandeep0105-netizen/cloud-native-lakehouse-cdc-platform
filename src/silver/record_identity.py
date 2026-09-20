from typing import Dict, Tuple

RECORD_IDENTITY: Dict[str, Tuple[str, ...]] = {
    'customers': ('customer_id',),
    'orders': ('order_id',),
    'products': ('product_id',),
    'sellers': ('seller_id',),
    'category_translation': ('product_category_name',),
    'order_items': ('order_id', 'order_item_id'),
    'order_payments': ('order_id', 'payment_sequential'),
    'order_reviews': ('order_review_key',),
    'geolocation': ('geolocation_id',),
}

SOURCE_TRACE_COLUMNS = {
    'order_reviews': 'review_id',
    'geolocation': 'geolocation_id',
}

def identity_columns(dataset: str) -> Tuple[str, ...]:
    if dataset not in RECORD_IDENTITY:
        raise ValueError(f'Unsupported dataset: {dataset}')
    return RECORD_IDENTITY[dataset]

def validate_identity_columns(dataset: str, columns: list[str]) -> None:
    required = identity_columns(dataset)
    missing = [column for column in required if column not in columns]
    if missing:
        raise ValueError(f'Missing identity columns for {dataset}: {missing}')

def validate_identity_contract() -> None:
    assert identity_columns('customers') == ('customer_id',)
    assert identity_columns('orders') == ('order_id',)
    assert identity_columns('products') == ('product_id',)
    assert identity_columns('sellers') == ('seller_id',)
    assert identity_columns('category_translation') == ('product_category_name',)
    assert identity_columns('order_items') == ('order_id', 'order_item_id')
    assert identity_columns('order_payments') == ('order_id', 'payment_sequential')
    assert identity_columns('order_reviews') == ('order_review_key',)
    assert identity_columns('geolocation') == ('geolocation_id',)
    assert SOURCE_TRACE_COLUMNS['order_reviews'] == 'review_id'
    assert SOURCE_TRACE_COLUMNS['geolocation'] == 'geolocation_id'

if __name__ == '__main__':
    validate_identity_contract()
    print('21-AV: RECORD IDENTITY CONTRACT PASS')
