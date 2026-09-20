# Project 02 — Silver CDC State Persistence Contract

## Purpose
- Define the persistent state required to apply governed CDC events to Silver Iceberg tables.
- Preserve the established source identity, ordering, deduplication, replay, and traceability contracts.

## State Requirements
- Silver business state is reconstructed from the Area 19 Iceberg snapshot plus valid CDC events.
- CDC application must be deterministic and idempotent.
- Duplicate event identities must not create additional state changes.
- An event with a source position older than or equal to the latest accepted position for the same record identity must not overwrite newer state.
- INSERT creates or establishes the record state.
- UPDATE changes the existing record state while preserving the governed record identity.
- DELETE removes the active business record state while retaining sufficient CDC metadata for auditability.

## CDC Metadata
- event_id
- operation
- source_position
- event_timestamp
- processed_at
- record_version

## Source Identity Rules
- customers: customer_id
- orders: order_id
- products: product_id
- sellers: seller_id
- category_translation: product_category_name
- order_items: (order_id, order_item_id)
- order_payments: (order_id, payment_sequential)
- order_reviews: review_id is not a sole key; operational order_review_key remains the technical row identity where available.
- geolocation: no reliable source primary key; operational geolocation_id remains the technical row identity where available.
- Technical keys must not overwrite source identifiers.

## Persistence Boundary
- Silver Iceberg tables are the persistent analytical business-state layer.
- CDC application state must be recoverable after process restart.
- Deduplication state must not depend solely on Python process memory.
- Raw, Bronze, and Area 19 source tables remain unchanged.

## Replay and Recovery
- Area 13 ordering rules remain authoritative.
- Area 14 event identity and idempotency rules remain authoritative.
- Area 15 checkpoint and replay rules remain authoritative.
- Reprocessing an already accepted event must produce no additional state change.

## Claim Boundary
- Local Iceberg implementation is verified locally.
- Historical Olist CDC remains simulated/replayed unless captured from the local PostgreSQL source.
- AWS execution is not claimed.

## Status
Draft — Area 21
