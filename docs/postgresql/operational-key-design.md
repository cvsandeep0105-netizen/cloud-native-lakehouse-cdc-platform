# Project 02 — Operational Key Design Decision

## Order Reviews
- review_id is retained as a source identifier.
- review_id is not used as the sole primary key because Area 07 and Area 08 profiling found 789 duplicated review_id groups covering 1,603 rows.
- Duplicate review_id groups were associated with the same order_id in the observed source data.
- A PostgreSQL technical surrogate key will provide row-level identity without modifying the source data.

## Geolocation
- geolocation_zip_code_prefix is not a sufficient key because only 19,015 unique ZIP prefixes exist across 1,000,163 source rows.
- Exact duplicate source rows exist: 261,831.
- The combination of ZIP prefix, latitude, and longitude still does not uniquely identify every source row.
- A PostgreSQL technical surrogate key will provide physical row identity.
- All original source columns will be preserved.

## Source Preservation
- No source rows will be removed during operational loading.
- No source values will be altered to satisfy primary-key constraints.
- Technical keys identify physical operational rows; source identifiers remain available for reconciliation and CDC processing.

## Decision Status
Accepted for Area 08 operational schema implementation.
