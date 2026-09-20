# Project 02 — Key & Relationship Source Contracts

## Contract Status
Status: Draft — Area 09

## Primary and Candidate Keys
- customers: customer_id
- orders: order_id
- products: product_id
- sellers: seller_id
- category_translation: product_category_name
- order_items: (order_id, order_item_id)
- order_payments: (order_id, payment_sequential)
- order_reviews: review_id is a source identifier but is not contractually unique.
- geolocation: no reliable source primary key; downstream technical key is permitted.

## Technical Key Rules
- Technical keys may be introduced only where the source does not provide a reliable unique identifier.
- Technical keys must not replace or overwrite source identifiers.
- Technical keys must be stable for the lifetime of the loaded operational record.

## Foreign-Key Relationships
- orders.customer_id -> customers.customer_id
- order_items.order_id -> orders.order_id
- order_items.product_id -> products.product_id
- order_items.seller_id -> sellers.seller_id
- order_payments.order_id -> orders.order_id
- order_reviews.order_id -> orders.order_id

## Relationship Contract Rules
- Foreign-key references must resolve to an existing parent record before dependent processing is accepted.
- Orphan references must be detected and reported.
- Referential-integrity failures must not be silently repaired.
- Existing source relationships are expected to be preserved through the operational representation.
- Relationship validation must be deterministic and auditable.

## Observed Baseline
- Area 07 profiling established 100% relationship coverage for all documented relationships.
- Area 08 PostgreSQL validation established zero orphan references for all six operational foreign-key relationships.
- These observed results are validation evidence, not permanent assumptions about future source deliveries.

## Special Source Cases
- order_reviews contains duplicate review_id values; review_id must therefore not be treated as the sole operational primary key.
- geolocation contains exact duplicate source rows; duplicates must be preserved rather than silently removed.
- Source identifiers and source relationships must remain traceable into downstream processing.

## Change Control
Any key or relationship change requires documented impact assessment, validation, and approval before dependent pipeline changes.
