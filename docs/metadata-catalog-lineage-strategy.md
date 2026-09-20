# Area 27-A — Metadata, Catalog & Lineage Strategy

## Purpose

Define the metadata, catalog, ownership, discovery, and lineage foundation for the Project 02 cloud-native lakehouse.

## Scope

- Source dataset metadata
- Raw, Bronze, Silver, and Gold layer metadata
- Iceberg table metadata
- Schema and column metadata
- Dataset ownership and stewardship
- Business definitions and metric ownership
- Technical lineage from source through Gold
- CDC and incremental-processing metadata references
- Metadata freshness and update expectations

## Catalog Boundary

- Local Apache Iceberg catalogs are authoritative for the current local development lakehouse.
- AWS Glue Data Catalog is the planned cloud production catalog.
- AWS Glue execution is NOT claimed by this local implementation.
- Metadata design must remain portable between local Iceberg and AWS Glue.

## Lineage Boundary

Lineage will represent the logical flow:

Source -> PostgreSQL -> CDC -> Raw -> Bronze -> Iceberg/Silver -> Gold

- Source-to-PostgreSQL lineage is documented.
- CDC lineage identifies change-event flow and processing boundaries.
- Raw and Bronze lineage identifies artifact transformation.
- Silver lineage identifies current-state CDC application.
- Gold lineage identifies authoritative Silver inputs and business metrics.

## Metadata Classes

1. Dataset metadata
2. Schema metadata
3. Column metadata
4. Key and relationship metadata
5. Pipeline metadata
6. CDC metadata
7. Quality metadata
8. Business metric metadata
9. Ownership and stewardship metadata
10. Lineage metadata

## Production Safety

- Metadata work must not mutate PostgreSQL source data.
- Metadata work must not rewrite Raw, Bronze, Silver, or Gold data.
- Existing Iceberg tables remain unchanged.
- Metadata registration must be additive and independently validated.

## Area 27 Acceptance Gates

- Metadata strategy documented: PASS
- Catalog boundary documented: PASS
- Local Iceberg authority documented: PASS
- AWS Glue production boundary documented: PASS
- End-to-end lineage model documented: PASS
- Metadata classes documented: PASS
- Production mutation boundary documented: PASS

## Status

Area 27-A is the metadata and lineage design foundation. Implementation and validation occur in subsequent Area 27 steps.
