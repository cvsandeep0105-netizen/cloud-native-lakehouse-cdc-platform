# Area 19 — Iceberg Table Contract

## Source
Validated Bronze Parquet datasets.

## Target
One Iceberg table per Olist dataset.

## Required Properties
- Table schema must represent the Bronze dataset.
- Table metadata must be independently inspectable.
- Table creation must be deterministic.
- Table state must be snapshot-aware.
- No business aggregation is performed.
- No Silver-level enrichment is performed.

## Integrity
Source-to-Iceberg row counts and schema compatibility must be validated before Area 19 acceptance.

## Idempotency
Repeated table initialization must not silently create conflicting table definitions.

## AWS Boundary
Local catalog/table validation only. AWS execution is not claimed.
