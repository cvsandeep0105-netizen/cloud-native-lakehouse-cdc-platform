# Area 24 - Gold Data Product Strategy

## Purpose

Define business-facing Gold data products derived from validated Silver data. Gold products must provide stable, documented analytical interfaces without changing Bronze or Silver semantics.

## Business Objectives

- Provide trusted order and customer analytics.
- Provide product and seller performance analytics.
- Provide payment and review analytics.
- Support incremental refresh from the Silver CDC processing layer.
- Keep business logic explicit, reproducible, and testable.

## Gold Product Principles

- Gold is consumption-oriented.
- Gold logic must use validated Silver data.
- Gold products must not directly depend on raw source files.
- Business metrics require explicit definitions.
- Grain must be documented for every product.
- Keys and joins must preserve Silver identity semantics.
- Null and unknown handling must be explicit.
- Duplicate business facts must not be introduced.
- CDC processing must remain compatible with incremental refresh.

## Initial Gold Products

### 1. Order Performance Product

Grain: one row per order.

Business purpose:
- Order lifecycle analysis
- Order value and freight analysis
- Delivery performance
- Customer and geographic analysis

### 2. Customer Analytics Product

Grain: one row per customer.

Business purpose:
- Customer order frequency
- Customer spending
- Customer purchase activity
- Customer geographic distribution

### 3. Product Performance Product

Grain: one row per product.

Business purpose:
- Product sales performance
- Order-item volume
- Revenue and freight analysis
- Product category analysis

### 4. Seller Performance Product

Grain: one row per seller.

Business purpose:
- Seller order-item volume
- Seller revenue
- Freight contribution
- Seller geographic analysis

### 5. Payment Analytics Product

Grain: one row per order-payment record.

Business purpose:
- Payment method analysis
- Payment value
- Installment analysis
- Payment behavior

### 6. Review Analytics Product

Grain: one row per operational review identity.

Business purpose:
- Review score analysis
- Review timing
- Review coverage
- Customer feedback analytics

## Metric Governance

Every Gold metric must document:
- Metric name
- Business definition
- Grain
- Source Silver datasets
- Join logic
- Null handling
- Deduplication rule
- Incremental refresh behavior
- Validation rule

## Data Quality Boundary

Gold processing must not silently repair upstream Silver defects. Invalid or unresolved records must follow documented quarantine or exclusion rules, with counts captured as evidence.

## Incremental Boundary

Gold products must support controlled incremental processing using the existing checkpoint and CDC framework. Gold processing must not bypass checkpoint ordering, deduplication, or idempotency guarantees.

## Production Safety

- Area 24-A creates documentation only.
- Production Bronze tables are not modified.
- Production Silver tables are not modified.
- Existing Gold directories are not modified during strategy definition.
- PostgreSQL is not modified.
- AWS execution is not claimed.

## Area 24-A Acceptance

- Business objectives defined.
- Gold products defined.
- Grain defined for each product.
- Metric governance defined.
- Data-quality boundary defined.
- Incremental boundary defined.
- Production safety boundary defined.

## Status

24-A: PASS
NEXT: 24-B - Gold Product Data Contracts
