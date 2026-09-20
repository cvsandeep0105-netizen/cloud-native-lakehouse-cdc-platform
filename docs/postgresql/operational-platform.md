# Project 02 — Operational PostgreSQL Platform

## Purpose
PostgreSQL is the operational relational representation of the Olist source data for Project 02.

## Database Boundary
- PostgreSQL is the local operational source platform.
- The database will preserve relational keys and source relationships.
- Source data will be loaded into a dedicated Project 02 schema.
- CDC infrastructure remains logically separate from analytical lakehouse layers.

## CDC Boundary
- Genuine PostgreSQL logical CDC was verified in Area 02.
- Historical Olist CSV data is static.
- Any changes generated from the historical dataset are CDC simulation/replay unless genuine CDC evidence exists.
- PostgreSQL logical replication will be used where appropriate for local CDC validation.

## Data Layer Boundary
- PostgreSQL: operational relational representation.
- S3 Raw: immutable ingestion boundary.
- Bronze: structurally normalized ingestion layer.
- Iceberg/Silver: incremental analytical processing layer.
- Gold: business data products.

## Security Boundary
- Credentials must not be committed to Git.
- Runtime secrets must come from secure environment/configuration mechanisms.
- Database access should follow least-privilege principles.

## Change Control
- Existing PostgreSQL configuration will not be modified unless required by a later approved Area.
- Table creation and schema changes will be validated before downstream CDC processing.
- Completed Areas remain frozen unless evidence requires reopening them.
