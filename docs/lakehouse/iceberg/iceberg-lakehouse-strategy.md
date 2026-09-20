# Area 19 — Apache Iceberg Lakehouse Strategy

## Purpose
Apache Iceberg provides the table-format layer for reliable analytical datasets downstream of the validated Bronze layer.

## Input Boundary
Area 19 consumes validated Bronze Parquet datasets established in Area 18.

## Table Format
Apache Iceberg is the target analytical table format.

## Core Capabilities
- Snapshot-based table state
- Atomic table updates
- Schema-aware metadata
- Table-level evolution capability
- Reliable analytical reads
- Separation of table metadata from business data processing

## Processing Boundary
Area 19 establishes Iceberg tables. Business-level Silver transformations are deferred to Area 21.

## CDC Boundary
CDC deduplication, replay, late-event handling, and backfill remain governed by Areas 13–15. Area 19 does not redefine those contracts.

## AWS Boundary
Local Iceberg implementation and validation do not constitute AWS Glue Catalog, S3, Athena, or production deployment evidence.
