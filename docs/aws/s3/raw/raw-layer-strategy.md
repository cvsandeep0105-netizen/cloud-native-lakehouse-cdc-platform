# Area 17 — Raw Immutable Data Layer

## Purpose
Establish the immutable raw ingestion boundary for Project 02.

## Raw Principles
- Raw data preserves source fidelity.
- Accepted raw objects are treated as immutable.
- Raw ingestion must be replayable.
- Source data must not be silently transformed at the raw boundary.
- New deliveries create new controlled ingestion artifacts.

## Olist Boundary
The Olist dataset is static historical source data. Its original CSV artifacts remain the acquisition truth.

## CDC Boundary
CDC events captured from PostgreSQL are separate raw change artifacts. Historical Olist change generation remains CDC simulation/replay.

## Storage
The planned AWS durable storage target is Amazon S3. Local validation uses the Project 02 lakehouse directory structure.

## Downstream
Bronze processing consumes the raw boundary in Area 18.
