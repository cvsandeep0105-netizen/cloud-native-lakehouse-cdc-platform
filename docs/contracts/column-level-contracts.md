# Project 02 — Column-Level Source Contracts

## Contract Status
Status: Draft — Area 09

## customers
| Column | Logical Type | Nullable |
|---|---|---|
| customer_id | string | No |
| customer_unique_id | string | No |
| customer_zip_code_prefix | integer | No |
| customer_city | string | No |
| customer_state | string | No |

## geolocation
| Column | Logical Type | Nullable |
|---|---|---|
| geolocation_zip_code_prefix | integer | No |
| geolocation_lat | decimal/double | No |
| geolocation_lng | decimal/double | No |
| geolocation_city | string | No |
| geolocation_state | string | No |

## order_items
| Column | Logical Type | Nullable |
|---|---|---|
| order_id | string | No |
| order_item_id | integer | No |
| product_id | string | No |
| seller_id | string | No |
| shipping_limit_date | timestamp | No |
| price | decimal | No |
| freight_value | decimal | No |

## order_payments
| Column | Logical Type | Nullable |
|---|---|---|
| order_id | string | No |
| payment_sequential | integer | No |
| payment_type | string | No |
| payment_installments | integer | No |
| payment_value | decimal | No |

## order_reviews
| Column | Logical Type | Nullable |
|---|---|---|
| review_id | string | No |
| order_id | string | No |
| review_score | integer | No |
| review_comment_title | string | Yes |
| review_comment_message | string | Yes |
| review_creation_date | timestamp | No |
| review_answer_timestamp | timestamp | No |

## orders
| Column | Logical Type | Nullable |
|---|---|---|
| order_id | string | No |
| customer_id | string | No |
| order_status | string | No |
| order_purchase_timestamp | timestamp | No |
| order_approved_at | timestamp | Yes |
| order_delivered_carrier_date | timestamp | Yes |
| order_delivered_customer_date | timestamp | Yes |
| order_estimated_delivery_date | timestamp | No |

## products
| Column | Logical Type | Nullable |
|---|---|---|
| product_id | string | No |
| product_category_name | string | Yes |
| product_name_lenght | integer | Yes |
| product_description_lenght | integer | Yes |
| product_photos_qty | integer | Yes |
| product_weight_g | integer | Yes |
| product_length_cm | integer | Yes |
| product_height_cm | integer | Yes |
| product_width_cm | integer | Yes |

## sellers
| Column | Logical Type | Nullable |
|---|---|---|
| seller_id | string | No |
| seller_zip_code_prefix | integer | No |
| seller_city | string | No |
| seller_state | string | No |

## category_translation
| Column | Logical Type | Nullable |
|---|---|---|
| product_category_name | string | No |
| product_category_name_english | string | No |

## Column Contract Rules
- Column names must match the registered source schema unless an approved schema-evolution change exists.
- Logical type changes must be explicitly detected and reviewed.
- Nullable fields must not be silently converted into non-null values.
- Required fields must be validated before downstream processing.
- Timestamp fields must be parseable when populated.
- Numeric fields must preserve source precision and semantic meaning.
- Source column values must remain unchanged in the immutable raw boundary.
