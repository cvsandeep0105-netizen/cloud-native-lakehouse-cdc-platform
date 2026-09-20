# Project 02 — Source Data Profiling Evidence

## Profiling Boundary
- Source files were analyzed read-only.
- No source CSV was modified.
- Profiling covers file structure, schema, nulls, uniqueness, relationships, value ranges, and timestamp parseability.

## Source Inventory
- CSV files: 9
- Source boundary: data/raw/olist/extracted/

## File-Level Baseline
- customers: 99,441 rows / 5 columns
- geolocation: 1,000,163 rows / 5 columns
- order_items: 112,650 rows / 7 columns
- order_payments: 103,886 rows / 5 columns
- order_reviews: 99,224 rows / 7 columns
- orders: 99,441 rows / 8 columns
- products: 32,951 rows / 9 columns
- sellers: 3,095 rows / 4 columns
- category_translation: 71 rows / 2 columns

## Null Findings
- customers: no nulls
- geolocation: no nulls
- order_items: no nulls
- order_payments: no nulls
- order_reviews: review_comment_title=87,656; review_comment_message=58,247
- orders: order_approved_at=160; order_delivered_carrier_date=1,783; order_delivered_customer_date=2,965
- products: product_category_name=610; product_name_lenght=610; product_description_lenght=610; product_photos_qty=610; physical dimensions/weight=2 each
- sellers: no nulls
- category_translation: no nulls

## Uniqueness & Duplicate Findings
- customers.customer_id: unique
- customers.customer_unique_id: not unique
- geolocation: 261,831 exact duplicate rows
- order_items: (order_id, order_item_id) is the candidate row key
- order_payments: (order_id, payment_sequential) is the candidate row key
- orders.order_id: unique
- products.product_id: unique
- sellers.seller_id: unique
- category_translation.product_category_name: unique

## Relationship Coverage
- orders.customer_id -> customers.customer_id: 100%
- order_items.order_id -> orders.order_id: 100%
- order_items.product_id -> products.product_id: 100%
- order_items.seller_id -> sellers.seller_id: 100%
- payments.order_id -> orders.order_id: 100%
- reviews.order_id -> orders.order_id: 100%
- translated category -> product category: 100%

## Value-Quality Findings
- order_items.price <= 0: 0
- order_items.freight_value < 0: 0
- payments.payment_value <= 0: 9
- payments.payment_installments <= 0: 2
- review_score outside 1-5: 0
- products.product_weight_g <= 0: 4
- product dimensions <= 0: 0
- geolocation latitude outside -90..90: 0
- geolocation longitude outside -180..180: 0

## Timestamp Parseability
- All five order timestamp columns had 0 invalid non-null values.

## Interpretation Boundary
- Findings describe the source dataset and are not source-data corrections.
- Raw source files remain immutable.
- Any cleansing, normalization, deduplication, type casting, or business-rule handling belongs to downstream processing layers.
