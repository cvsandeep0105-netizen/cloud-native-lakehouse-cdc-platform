# Area 20 — File Layout & Storage Optimization Policy

## Current Baseline

The local Apache Iceberg Olist foundation currently contains one Parquet data file per table.

| Table | Data Files | Approx. Data Size |
|---|---:|---:|
| category_translation | 1 | <0.01 MB |
| customers | 1 | 3.86 MB |
| geolocation | 1 | 13.59 MB |
| order_items | 1 | 3.73 MB |
| order_payments | 1 | 2.15 MB |
| order_reviews | 1 | 5.29 MB |
| orders | 1 | 5.97 MB |
| products | 1 | 0.81 MB |
| sellers | 1 | 0.07 MB |

## File-Size Policy

For production-scale analytical workloads, the platform targets approximately 128–512 MB per data file where workload and table size justify that range.

This is a target range, not a requirement for every table.

Small reference or dimension tables are not artificially expanded or rewritten merely to satisfy a file-size target.

## Small-File Policy

Compaction is triggered by file-count and workload evidence, particularly when incremental CDC ingestion creates excessive small files.

The current Olist snapshot has one data file per table and therefore does not require compaction.

## Current Decision

No file rewrite or compaction is required for the current snapshot.

Future incremental/CDC workloads will be evaluated for small-file accumulation and compaction requirements.

## Partitioning Boundary

Partitioning is selective rather than universal. The current Olist snapshot does not require immediate partition rewrites.

The `orders.order_purchase_timestamp` column remains the primary candidate for future time-based partitioning if query volume and workload justify it.

## Optimization Principle

Optimize for query patterns, file counts, table growth, and operational evidence rather than applying partitioning or compaction mechanically.
