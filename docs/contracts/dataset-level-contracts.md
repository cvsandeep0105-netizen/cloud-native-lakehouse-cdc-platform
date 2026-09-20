# Project 02 — Dataset-Level Source Contracts

## Contract Status
Status: Draft — Area 09

## customers
- Source file: olist_customers_dataset.csv
- Grain: One customer record per customer_id.
- Observed source rows: 99,441.
- Primary source identifier: customer_id.
- Source role: Customer master / order customer reference.

## geolocation
- Source file: olist_geolocation_dataset.csv
- Grain: One geolocation observation per source row; duplicate source rows are preserved.
- Observed source rows: 1,000,163.
- Source identifier: No reliable source primary key; technical key is permitted downstream.
- Source role: Geographic reference data.

## order_items
- Source file: olist_order_items_dataset.csv
- Grain: One order-item record per order_id and order_item_id.
- Observed source rows: 112,650.
- Composite source key: order_id + order_item_id.
- Source role: Order line-item facts.

## order_payments
- Source file: olist_order_payments_dataset.csv
- Grain: One payment record per order_id and payment_sequential.
- Observed source rows: 103,886.
- Composite source key: order_id + payment_sequential.
- Source role: Order payment facts.

## order_reviews
- Source file: olist_order_reviews_dataset.csv
- Grain: One source review record per physical source row.
- Observed source rows: 99,224.
- Source identifier: review_id is retained but is not assumed to be unique.
- Source role: Order review records.

## orders
- Source file: olist_orders_dataset.csv
- Grain: One order record per order_id.
- Observed source rows: 99,441.
- Primary source identifier: order_id.
- Source role: Order lifecycle / transaction header.

## products
- Source file: olist_products_dataset.csv
- Grain: One product record per product_id.
- Observed source rows: 32,951.
- Primary source identifier: product_id.
- Source role: Product master data.

## sellers
- Source file: olist_sellers_dataset.csv
- Grain: One seller record per seller_id.
- Observed source rows: 3,095.
- Primary source identifier: seller_id.
- Source role: Seller master data.

## category_translation
- Source file: product_category_name_translation.csv
- Grain: One translation record per product_category_name.
- Observed source rows: 71.
- Primary source identifier: product_category_name.
- Source role: Product category reference / translation.

## Dataset-Level Contract Rules
- Expected source files must be present before ingestion.
- Dataset identity must match the registered Olist source.
- Unexpected missing datasets must block dependent processing.
- Source row counts are observed acquisition/profiling evidence and must not be treated as permanent future row-count constants.
- Source files are immutable acquisition artifacts.
- Source values must not be silently modified to satisfy downstream contracts.
- Contract changes require documented change control.
