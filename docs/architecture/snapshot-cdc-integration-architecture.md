# Project 02 — Snapshot and CDC Integration Architecture

## Purpose
This document defines how the initial source snapshot and subsequent CDC changes integrate into one consistent incremental data architecture.

## End-to-End Integration
Olist historical source files
? immutable acquisition boundary
? initial PostgreSQL operational snapshot
? snapshot completion checkpoint
? subsequent source changes
? CDC capture or controlled CDC simulation
? immutable raw CDC event boundary
? ordered incremental processing
? Bronze
? Iceberg
? Silver
? Gold

## Snapshot Phase
The initial snapshot loads the Olist source state into the project02 PostgreSQL operational representation.
Snapshot completion establishes the initial state boundary.
Snapshot row counts, schema, keys, relationships, and quality results must be validated before incremental processing begins.

## CDC Phase
After the snapshot boundary, subsequent changes are represented as CDC events.
Each event must identify its source dataset, source key, operation, ordering information, and relevant timestamp or equivalent metadata.
CDC events must remain distinguishable from snapshot records.

## State Transition Model
Snapshot establishes the initial target state.
INSERT adds a new source state.
UPDATE changes an existing source state.
DELETE removes or logically removes the corresponding source state according to the downstream table design.
State transitions must be deterministic and replayable.

## Integration Boundary
The snapshot and CDC paths must converge through a defined event/state-processing boundary rather than independently writing uncontrolled target state.
Downstream processing must know whether an input represents initial snapshot data or a change event.

## Ordering Boundary
CDC ordering must begin after the established snapshot boundary.
An event must not be applied before the corresponding snapshot state is available.
Source/event ordering metadata must be preserved.
Arrival time alone is insufficient as the authoritative ordering mechanism.

## Duplicate and Idempotency Boundary
Repeated delivery of the same CDC event must not create unintended duplicate target state.
Deduplication keys and idempotent application logic will be implemented and validated in Areas 13 and 14.

## Replay Boundary
Captured CDC events must support deterministic replay.
Replay must be distinguishable from normal forward processing.
Reprocessing must not corrupt the snapshot or create uncontrolled duplicate state.

## Late-Event Boundary
Events arriving after their expected processing position must be detected and handled according to explicit downstream policy.
Late-event handling will be implemented and validated in Area 15.

## Failure and Recovery
Snapshot completion state and CDC processing state must be independently observable.
Failures must not silently mark unprocessed events as complete.
Recovery must resume from a safe checkpoint or replay boundary.

## AWS Integration
In an AWS implementation, AWS DMS may provide full-load and CDC delivery into the planned S3 raw boundary.
Actual AWS DMS behavior must be validated in AWS before execution claims are made.

## Local Integration
Local PostgreSQL provides the verified logical-CDC capability.
The historical Olist source remains static, so generated historical changes are explicitly classified as CDC simulation/replay.

## Traceability
Snapshot records and CDC events must retain source dataset and source-key traceability into downstream processing.

## Claim Integrity
Area 02 provides verified local PostgreSQL CDC evidence.
Areas 06–09 provide verified Olist source, profiling, operational PostgreSQL, and source-contract foundations.
Snapshot-plus-CDC integration is the architecture being established here; downstream implementation capabilities are not claimed complete until their dedicated Areas are validated.
