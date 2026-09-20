# Area 24 - Gold Product Data Contracts

## Contract Principles

- Gold schemas are consumption-facing contracts.
- Each product has a declared grain.
- Every metric has an explicit definition.
- Silver remains the authoritative upstream analytical layer.
- Existing Silver column semantics are preserved.
- Gold products must be deterministic and incrementally maintainable.

## Product 1 - Order Performance

Grain: one row per order.

Required business fields:
- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date
- order_item_count
- order_gross_value
- order_freight_value
- order_total_value
- delivery_days
- delivery_delay_days

Metric definitions:
- order_item_count = count of order items for the order.
- order_gross_value = sum of item price.
- order_freight_value = sum of item freight value.
- order_total_value = order_gross_value + order_freight_value.
- delivery_days = delivered_customer_date - purchase_timestamp when both exist.
- delivery_delay_days = delivered_customer_date - estimated_delivery_date when both exist.

## Product 2 - Customer Analytics

Grain: one row per customer_id.

Required business fields:
- customer_id
- customer_unique_id
- customer_order_count
- customer_item_count
- customer_total_value
- customer_average_order_value
- first_order_timestamp
- last_order_timestamp

Metric definitions:
- customer_order_count = distinct orders associated with customer_id.
- customer_item_count = total order-item quantity across customer orders.
- customer_total_value = total order value across customer orders.
- customer_average_order_value = customer_total_value / customer_order_count when order count > 0.
- first_order_timestamp = earliest purchase timestamp.
- last_order_timestamp = latest purchase timestamp.

## Product 3 - Product Performance

Grain: one row per product_id.

Required business fields:
- product_id
- product_category_name
- product_order_count
- product_item_count
- product_units_value
- product_freight_value
- product_average_item_price

Metric definitions:
- product_order_count = distinct orders containing the product.
- product_item_count = number of order-item records for the product.
- product_units_value = sum of item price.
- product_freight_value = sum of freight value.
- product_average_item_price = average item price.

## Product 4 - Seller Performance

Grain: one row per seller_id.

Required business fields:
- seller_id
- seller_order_count
- seller_item_count
- seller_units_value
- seller_freight_value
- seller_average_item_price

Metric definitions:
- seller_order_count = distinct orders containing seller items.
- seller_item_count = number of order-item records for seller.
- seller_units_value = sum of item price.
- seller_freight_value = sum of freight value.
- seller_average_item_price = average item price.

## Product 5 - Payment Analytics

Grain: one row per order_id + payment_sequential.

Required business fields:
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

Metric definitions:
- payment_value = operational payment value from Silver.
- payment_installments = operational installment count from Silver.
- payment records retain their composite operational identity.

## Product 6 - Review Analytics

Grain: one row per order_review_key.

Required business fields:
- order_review_key
- review_id
- order_id
- review_score
- review_creation_date
- review_answer_timestamp

Metric definitions:
- review_score = operational review score.
- review_creation_date = operational review creation timestamp.
- review_answer_timestamp = operational review answer timestamp.
- order_review_key is the technical identity established by the operational model.

## Null Handling

- Missing optional timestamps remain NULL.
- Missing optional descriptive attributes remain NULL.
- Division metrics return NULL when their denominator is zero.
- Nulls must not be silently converted into zero unless the metric definition explicitly requires zero.

## Deduplication

- Order metrics use order_id as order grain.
- Customer metrics use customer_id as customer grain.
- Product metrics use product_id as product grain.
- Seller metrics use seller_id as seller grain.
- Payment metrics preserve order_id + payment_sequential.
- Review metrics preserve order_review_key.
- Gold processing must not invent replacement identities.

## Source Mapping

- Orders: Silver orders.
- Customers: Silver customers.
- Order items: Silver order_items.
- Products: Silver products.
- Sellers: Silver sellers.
- Payments: Silver order_payments.
- Reviews: Silver order_reviews.
- Category enrichment: Silver category_translation when required.

## Incremental Contract

- Gold products consume validated Silver state.
- CDC updates must be applied according to the existing checkpoint boundary.
- Reprocessing the same source state must produce the same Gold result.
- Duplicate CDC deliveries must not create duplicate Gold facts.

## Area 24-B Acceptance

- Six Gold products defined.
- Grain defined for every product.
- Business fields defined.
- Metric definitions defined.
- Null handling defined.
- Identity and deduplication rules defined.
- Silver source mapping defined.
- Incremental compatibility defined.

## Status

24-B: PASS
NEXT: 24-C - Gold Product Implementation Design
