# Area 24 - Gold Product Implementation Design

## Implementation Principles

- Gold processing consumes validated Silver state only.
- Each product is built at its declared grain.
- Joins must use documented operational identities.
- Aggregations must be deterministic.
- Business calculations must be reproducible.
- Incremental processing must respect existing checkpoint boundaries.
- Gold processing must be independently testable.

## Product 1 - Order Performance

Implementation flow:
1. Read Silver orders.
2. Aggregate Silver order_items by order_id.
3. Aggregate item price and freight values.
4. Join order-level aggregates to Silver orders.
5. Calculate lifecycle and delivery metrics.
6. Validate one output row per order_id.

Primary join:
- orders.order_id = order_items.order_id

Validation:
- Output order_id uniqueness.
- Order count reconciliation.
- Item-count reconciliation.
- Monetary aggregation reconciliation.

## Product 2 - Customer Analytics

Implementation flow:
1. Read Silver customers.
2. Read Silver orders.
3. Aggregate order activity by customer_id.
4. Join customer attributes.
5. Calculate order count, item count, value, average order value, and activity timestamps.
6. Validate one output row per customer_id.

Primary join:
- customers.customer_id = orders.customer_id

Additional aggregation:
- orders joined to order_items through order_id for item-level metrics.

## Product 3 - Product Performance

Implementation flow:
1. Read Silver products.
2. Read Silver order_items.
3. Aggregate item activity by product_id.
4. Join product attributes.
5. Enrich category using category_translation where applicable.
6. Calculate product metrics.
7. Validate one output row per product_id.

Primary join:
- products.product_id = order_items.product_id

## Product 4 - Seller Performance

Implementation flow:
1. Read Silver sellers.
2. Read Silver order_items.
3. Aggregate item activity by seller_id.
4. Join seller attributes.
5. Calculate seller metrics.
6. Validate one output row per seller_id.

Primary join:
- sellers.seller_id = order_items.seller_id

## Product 5 - Payment Analytics

Implementation flow:
1. Read Silver order_payments.
2. Preserve order_id + payment_sequential as the output identity.
3. Carry payment type, installments, and payment value.
4. Validate composite-key uniqueness.

Primary identity:
- order_id + payment_sequential

## Product 6 - Review Analytics

Implementation flow:
1. Read Silver order_reviews.
2. Preserve order_review_key as technical identity.
3. Carry review attributes and timestamps.
4. Validate review-score domain.
5. Validate one output row per order_review_key.

Primary identity:
- order_review_key

## Join Safety

- No many-to-many join may be introduced unintentionally.
- Pre-aggregation is required before joining one-to-many relationships when the target grain is higher.
- Join cardinality must be validated.
- Unmatched records must be measured.
- Row multiplication must be detected.

## Incremental Strategy

- Silver remains the authoritative state.
- Gold rebuilds and incremental updates must produce equivalent results.
- Changed Silver entities determine affected Gold entities.
- Checkpoints are not independently advanced by Gold outside the established incremental framework.
- Duplicate source deliveries must not create duplicate Gold records.

## Determinism

- Same Silver input state must produce the same Gold output.
- Aggregation ordering must not change metric values.
- NULL handling follows the Area 24-B contract.
- Technical identities are preserved.

## Validation Gates

- Schema validation.
- Grain uniqueness.
- Source-to-Gold row reconciliation.
- Aggregate metric reconciliation.
- Join-cardinality validation.
- NULL-rule validation.
- Duplicate detection.
- Incremental versus full-result equivalence.

## Production Safety

- Area 24-C is design-only.
- Production Gold tables are not created or modified.
- Production Silver remains unchanged.
- PostgreSQL remains unchanged.
- AWS execution is not claimed.

## Area 24-C Acceptance

- Six implementation flows defined.
- Join strategy defined.
- Aggregation strategy defined.
- Grain validation defined.
- Incremental strategy defined.
- Determinism requirements defined.
- Validation gates defined.

## Status

24-C: PASS
NEXT: 24-D - Controlled Gold Product Build
