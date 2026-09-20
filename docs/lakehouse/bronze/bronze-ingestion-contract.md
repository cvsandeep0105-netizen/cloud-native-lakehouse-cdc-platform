# Area 18 — Bronze Ingestion Contract

## Input
Nine Olist CSV artifacts from the immutable Raw layer.

## Output
Nine corresponding Bronze Parquet datasets.

## Required Guarantees
- One Bronze dataset per source dataset.
- Source business columns are preserved.
- Record counts are reconcilable.
- No silent row filtering.
- No business-level aggregation.
- No analytical enrichment.
- Deterministic output.

## Data Quality Boundary
Bronze does not replace the deterministic data-quality controls defined by the project data contracts.

## Failure Behavior
Processing fails explicitly when an expected source artifact is missing or structurally incompatible.

## AWS Boundary
This contract is locally validated and does not claim AWS execution.
