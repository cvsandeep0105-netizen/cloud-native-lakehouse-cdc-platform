# Project 02 — CDC Architecture Principles

## Purpose
This document defines the architectural principles governing Change Data Capture for Project 02.

## Source Boundary
The published Olist dataset is a static historical dataset.
It is the source for the initial operational snapshot.
It is not a native live CDC feed.

## CDC Strategy
Project 02 uses a layered CDC strategy.
The operational PostgreSQL platform provides a genuine local logical-CDC capability that was independently verified in Area 02.
Historical changes derived from the Olist dataset are classified explicitly as CDC simulation or replay.
AWS DMS remains an architectural option and is not considered executed without AWS runtime evidence.

## Snapshot and CDC Separation
Initial snapshot ingestion and subsequent change-event processing are separate logical stages.
The snapshot establishes the initial state.
CDC events represent changes applied after the snapshot boundary.
Downstream processing must preserve the distinction between snapshot records and change events.

## Change Event Principles
Every change event must identify its source dataset and source record key.
Every change event must contain an explicit operation type.
Supported operations are INSERT, UPDATE, and DELETE.
Event ordering information must be retained.
Event metadata must support traceability and replay.

## Source Preservation
CDC processing must preserve source identifiers and source values.
Raw change events must be immutable after capture.
Transformations belong in downstream processing layers rather than the raw CDC boundary.

## Idempotency
CDC processing must be designed for safe retries and repeated delivery.
Duplicate events must not create duplicate target state.
Deduplication and idempotency implementation will be validated in later Areas.

## Ordering
CDC processing must use an explicit deterministic ordering mechanism.
Ordering must be based on source/event metadata rather than arrival order alone.
Out-of-order and late events must be handled explicitly.

## Replay and Backfill
CDC architecture must support deterministic replay of captured events.
Backfill operations must be distinguishable from normal forward CDC processing.
Replay and backfill controls will be implemented and validated in later Areas.

## Reliability
CDC processing must support checkpoints or equivalent progress tracking.
Failures must not silently advance processing state.
Partial processing must be recoverable without corrupting target state.

## Security
CDC infrastructure must follow least-privilege access.
Replication credentials and secrets must never be committed to Git.
Sensitive configuration must be supplied through approved runtime configuration mechanisms.

## Observability
CDC processing must expose operational evidence including event counts, operation counts, processing state, failures, retries, and latency where applicable.

## Claim Integrity
Local PostgreSQL CDC capability is verified.
Historical Olist CDC is simulation/replay unless a genuine change source is independently demonstrated.
AWS DMS CDC execution, AWS throughput, AWS cost, and production behavior must not be claimed without corresponding AWS evidence.

## Change Control
Changes to CDC architecture, event semantics, ordering, reliability, or source boundaries require documented impact assessment and validation.
