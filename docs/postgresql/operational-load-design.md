# Project 02 — Operational PostgreSQL Load Design

## Load Objective
- Load the immutable Olist CSV source files into the project02 PostgreSQL schema without modifying source files.
- Preserve source row counts and source values.

## Load Order
1. customers
2. products
3. sellers
4. category_translation
5. orders
6. order_items
7. order_payments
8. order_reviews
9. geolocation

## Dependency Principle
- Parent/reference tables are loaded before tables containing foreign keys.
- Foreign-key constraints remain active during loading.
- A failed load must not be silently treated as successful.

## Source Preservation
- CSV files under data/raw/olist/extracted remain immutable.
- PostgreSQL loading is a representation of the source, not a source-data correction process.
- Null values remain null where permitted by the operational schema.

## Validation
- Each table will be checked against the corresponding source row count.
- Primary-key violations must be zero.
- Foreign-key violations must be zero.
- Loaded PostgreSQL data will be reconciled against the source dataset before the operational platform is accepted.

## CDC Boundary
- This initial load is a snapshot operation.
- It is not itself CDC.
- CDC event generation/capture remains governed by later Project 02 Areas.
