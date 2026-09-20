# Project 02 — Operational Relational Model

## Schema
- Database: postgres
- Schema: project02
- Owner: postgres

## Source Tables
| Source Dataset | Operational Table | Primary Key / Candidate Key |
|---|---|---|
| customers | project02.customers | customer_id |
| geolocation | project02.geolocation | No natural single-row key; composite/technical key required |
| orders | project02.orders | order_id |
| order_items | project02.order_items | (order_id, order_item_id) |
| payments | project02.order_payments | (order_id, payment_sequential) |
| reviews | project02.order_reviews | review_id requires validation before PK enforcement |
| products | project02.products | product_id |
| sellers | project02.sellers | seller_id |
| category_translation | project02.category_translation | category_name |

## Relationship Direction
- orders.customer_id references customers.customer_id.
- order_items.order_id references orders.order_id.
- order_items.product_id references products.product_id.
- order_items.seller_id references sellers.seller_id.
- order_payments.order_id references orders.order_id.
- order_reviews.order_id references orders.order_id.
- Product category values may be related to category_translation.category_name.

## Key Integrity Boundary
- Primary and foreign keys will be enforced only after source profiling findings are reconciled.
- The order_reviews review_id uniqueness finding from Area 07 must be resolved before declaring it a primary key.
- Geolocation has repeated rows by zip code and exact duplicate records; its physical key requires explicit design.
- Source data will not be modified to make it fit the relational model.

## CDC Readiness
- Tables must retain source identifiers required for future CDC events.
- CDC operation metadata will not be mixed into the original source columns.
- CDC capture and replay metadata will be introduced in the appropriate later Areas.
