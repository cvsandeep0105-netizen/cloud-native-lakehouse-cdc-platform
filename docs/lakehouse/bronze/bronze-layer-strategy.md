# Area 18 — Bronze Layer Strategy

## Purpose
The Bronze layer is the first structured processing layer downstream of the immutable Raw layer.

## Input Boundary
Input is the locally verified immutable Olist raw artifact layer established in Area 17.

## Transformation Boundary
Bronze preserves source business columns and source-level record content while applying controlled structural normalization required for downstream processing.

## Storage
Bronze artifacts are stored as Parquet.

## Source Truth
The original Olist dataset remains the historical source truth.

## CDC Boundary
CDC events are not merged into Bronze business tables in Area 18. CDC processing remains governed by the CDC architecture established in Areas 10–15.

## Reliability
Bronze processing must be deterministic, repeatable, auditable, and independently reconcilable to Raw.

## AWS Boundary
Area 18 local execution does not claim AWS Glue, S3, Athena, or other AWS execution.
