# Incremental Processing Framework

## Purpose
Area 22 defines the production-oriented incremental processing boundary between governed CDC events and downstream processing.

## Processing Model
1. Establish a source-position processing boundary.
2. Start after the persisted checkpoint when resuming.
3. Select only events inside the bounded interval.
4. Remove duplicate event deliveries by event_id.
5. Process events deterministically by source_position and event_id.
6. Advance the checkpoint only to successfully selected event positions.
7. Use the resulting checkpoint as the restart boundary for the next batch.

## Watermark
The source-position watermark represents the highest successfully selected source position in a processing batch.

## Restart Semantics
A restarted processor resumes from checkpoint_position + 1 for the same source system, schema, and table.

## Idempotency Boundary
Duplicate event deliveries are filtered by event_id before downstream application. Existing Area 21 persistent CDC controls remain authoritative for durable Silver mutation.

## Initial Snapshot + CDC Boundary
The Area 19 initial snapshot establishes the initial analytical state. Area 22 processes subsequent CDC positions without redefining the snapshot itself.

## Failure Boundary
A checkpoint must represent only successfully accepted processing progress. Failed batches must not advance the checkpoint.

## Scope
This area establishes the reusable incremental-processing framework. Durable orchestration and production failure recovery are handled by later Areas 29–32.

## AWS Boundary
The implementation is local and does not claim AWS execution.
