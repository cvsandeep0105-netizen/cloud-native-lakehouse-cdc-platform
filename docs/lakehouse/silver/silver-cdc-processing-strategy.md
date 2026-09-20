# Area 21-A — Silver CDC Processing Strategy

## Purpose
Define the Silver layer as the CDC-aware, business-ready state derived from the governed Bronze/Iceberg foundation.

## Processing Boundary
Silver consumes governed CDC events and the existing Iceberg analytical state. Raw and Bronze remain immutable.

## CDC Semantics
- INSERT creates a Silver record.
- UPDATE applies the latest valid change according to the authoritative source position.
- DELETE removes or logically retires the affected business record according to the table-specific contract.
- Duplicate events are rejected using the Area 14 deterministic event identity.
- Out-of-order and late events follow the Area 15 replay and checkpoint rules.

## Ordering
Silver application order follows the authoritative source-position ordering established in Area 13.

## Idempotency
Reprocessing an already-applied CDC event must not produce an additional business-state change.

## Replay & Backfill
Silver must support checkpoint-bounded replay and controlled backfill without corrupting the current authoritative state.

## Data Preservation
Business columns and source meaning are preserved. Silver transformations must be deterministic and explicitly documented.

## Traceability
Each applied CDC change must remain traceable to its source event identity and authoritative source position.

## Reliability Boundary
Failed events must not partially corrupt Silver state. Processing must support controlled retry or replay.

## Storage Boundary
Silver is implemented on the Project 02 Iceberg lakehouse foundation. AWS deployment is not claimed in Area 21.

## Dependency Boundaries
- Area 13: event ordering
- Area 14: deduplication and idempotency
- Area 15: replay, late events, and backfill
- Area 19: Iceberg lakehouse foundation
- Area 20: physical file-layout strategy

## Status
Area 21-A strategy: DEFINED
