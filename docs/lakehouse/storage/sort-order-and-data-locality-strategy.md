# Area 20-D — Sort Order & Data Locality Strategy

## Purpose
Define physical ordering and locality principles for the Project 02 Iceberg layer without introducing unnecessary rewrites or premature optimization.

## Current Snapshot
The current Olist snapshot contains one primary Parquet data file per Iceberg table. Current table sizes do not justify a broad repartitioning or compaction operation.

## Ordering Principles
- Physical ordering must support documented access patterns rather than arbitrary column sorting.
- Ordering must not alter business meaning, row counts, or source semantics.
- Ordering optimization must be evaluated together with partitioning, file size, workload, and future CDC growth.
- Small tables must not be artificially repartitioned.

## Primary Candidate
For the orders dataset, order_purchase_timestamp is the primary future locality candidate because it represents the principal business event time and is expected to support time-range analytical access.

## Secondary Locality Candidates
- orders.order_id may support point and join-oriented access patterns.
- order_items.order_id supports locality for order-level joins.
- order_payments.order_id supports locality for order-level joins.
- order_reviews.order_id supports locality for order-level joins.

## CDC Consideration
Future CDC processing may introduce additional files and change physical locality. Any optimization must preserve CDC ordering, deduplication, idempotency, replay, late-event, and backfill guarantees established in Areas 13–15.

## Current Implementation Decision
No global sort or repartition rewrite is performed during Area 20 for the current snapshot.

## Optimization Trigger
Consider physical ordering when measured query workload, table growth, partition distribution, CDC-generated file accumulation, or scan behavior demonstrates a material benefit.

## Validation Requirement
Any future ordering optimization must compare row counts, schema, table snapshots, file counts, file sizes, and representative query behavior before and after the change.

## Boundary
This document defines the Area 20-D strategy. It does not claim AWS deployment or production-scale benchmark results.
