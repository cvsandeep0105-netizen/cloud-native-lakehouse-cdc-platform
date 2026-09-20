# Project 02 — Area 21 Silver Identity Resolution

## Status
Controlled implementation validation.

## Standard Dataset Identities
- customers: customer_id
- orders: order_id
- products: product_id
- sellers: seller_id
- category_translation: product_category_name
- order_items: (order_id, order_item_id)
- order_payments: (order_id, payment_sequential)

## Special Operational Identities
- geolocation: PostgreSQL geolocation_id
- order_reviews: PostgreSQL order_review_key

## Preservation Rule
Original source columns remain preserved. Technical keys are additive operational identities and do not replace source identifiers.

## Validation
- PostgreSQL geolocation_id: 1,000,163 distinct keys across 1,000,163 rows.
- PostgreSQL order_review_key: 99,224 distinct keys across 99,224 rows.
- Silver special-key reconstruction completed from the authoritative operational representation.
- No new technical identifiers were fabricated.

## AWS Boundary
No AWS execution or AWS CDC service usage is claimed in Area 21.
