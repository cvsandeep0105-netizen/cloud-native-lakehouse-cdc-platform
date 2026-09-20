# Area 16 — S3 Storage Format Strategy

## Raw
Preserve source fidelity. Original CSV may remain at the acquisition boundary; CDC event landing may use JSONL where event structure requires it.

## Bronze
Parquet is the preferred standardized columnar representation.

## Silver
Apache Iceberg-managed Parquet is planned from Area 19 onward.

## Gold
Parquet/Iceberg-backed analytical products are planned according to downstream query requirements.

## Compression
Compression settings will be selected based on measured storage and processing behavior rather than arbitrary defaults.
