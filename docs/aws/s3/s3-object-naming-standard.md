# Area 16 — S3 Object Naming Standard

## Naming Principles
- Object paths must be deterministic.
- Paths must identify data layer, domain, table, and ingestion scope.
- Names must avoid ambiguous or environment-dependent naming.
- Raw objects must not be silently overwritten.

## Canonical Pattern
{layer}/{domain}/{table}/{partition}/object

## Example
raw/olist/orders/ingestion_date=YYYY-MM-DD/part-00000.parquet

## CDC Example
raw/olist/cdc/orders/ingestion_date=YYYY-MM-DD/part-00000.jsonl

## File Principles
- Prefer Parquet for analytical tabular data.
- Preserve JSON/JSONL when raw event fidelity requires it.
- Compression should be selected according to downstream processing requirements.
