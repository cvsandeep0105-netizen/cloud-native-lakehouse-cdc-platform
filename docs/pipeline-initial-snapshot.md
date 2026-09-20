# Project 02 — Initial Snapshot Pipeline

## Purpose
Define the controlled initial snapshot pipeline from immutable Olist source files into the Project02 operational PostgreSQL schema.

## Source Boundary
The nine acquired Olist CSV files under data/raw/olist/extracted are immutable source inputs.

## Target Boundary
The snapshot target is the project02 PostgreSQL schema established in Area 08.

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

## Processing Principles
The pipeline must preserve source values and source row counts.
Foreign-key constraints remain active during loading.
Null values remain null where permitted by the target schema.
No source correction or silent transformation is permitted.

## Transaction Boundary
Each dataset load must have an explicit success or failure outcome.
A failed dataset load must not be reported as successful.

## Validation
Each target table must reconcile to its corresponding source row count.
Primary-key violations must be zero.
Foreign-key violations must be zero.
Pipeline execution results must be recorded as evidence.

## Idempotency Boundary
Initial snapshot reruns must be controlled and must not silently duplicate target records.
The exact rerun strategy will be implemented and validated before snapshot acceptance.

## CDC Boundary
The initial snapshot is not CDC.
CDC processing begins only after the snapshot boundary is explicitly established.

## Failure Boundary
A failure must stop successful snapshot progression and expose the failing dataset and processing stage.
Recovery must not silently bypass validation.

## Observability
The pipeline must record dataset name, source row count, target row count, processing status, duration, and failure information where applicable.

## Claim Integrity
Local snapshot execution may be claimed only after runtime validation and reconciliation evidence.
AWS snapshot execution must not be claimed without AWS runtime evidence.

## Change Control
Changes to load order, target mapping, validation rules, transaction behavior, or rerun semantics require documented impact assessment and validation.
