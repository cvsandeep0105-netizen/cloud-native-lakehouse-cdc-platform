# Project 02 — CDC Reliability and Failure Boundaries

## Purpose
This document defines reliability and failure boundaries for the Project 02 CDC architecture.

## Reliability Principles
CDC processing must be restartable, observable, and deterministic.
Failures must not silently acknowledge or discard unprocessed change events.
Recovery must preserve source-event traceability.

## Capture Failure
If CDC capture fails, downstream processing must not advance beyond the last safely captured position.
Capture progress must be recoverable from the relevant source position or checkpoint.

## Consumer Failure
If a CDC consumer fails after receiving an event but before safely committing processing state, the event may be delivered again.
Downstream processing must therefore be designed for idempotent handling.

## Checkpoint Failure
Checkpoint state must represent only successfully processed input.
A checkpoint must not advance before the corresponding processing outcome is safely committed.

## Duplicate Delivery
Repeated delivery of the same event must be detectable using deterministic event identity or equivalent source metadata.
Duplicate handling must prevent unintended duplicate target state.

## Partial Processing
Multi-step processing must define a safe commit boundary.
Partial completion must be recoverable without silently losing or double-applying source changes.

## Restart
A restarted consumer must resume from a safe checkpoint or replay boundary.
Restart behavior must be deterministic and observable.

## Ordering Failure
Events received out of order must not be assumed to represent source order.
Ordering metadata must be retained and evaluated before state application.

## Late Events
Late events must be detected according to the defined ordering boundary.
Late-event policy will be implemented and validated in Area 15.

## Replay
Captured events must support controlled replay.
Replay must be distinguishable from normal forward processing.
Replay must not corrupt already processed target state.

## Backfill
Backfill processing must have an explicit scope and checkpoint boundary.
Backfill must not silently alter normal CDC progress.

## Snapshot Failure
If the initial snapshot fails, the CDC incremental boundary must not be treated as complete.
Snapshot completion must be explicitly established before normal CDC application begins.

## Observability
Reliability monitoring must expose processing position, event counts, operation counts, failures, retries, processing duration, and recovery status where applicable.

## Security Failure Boundary
Credential failures, authorization failures, and secret-access failures must be surfaced as operational failures.
Secrets must never be written into logs or source-controlled files.

## Local PostgreSQL Boundary
Local PostgreSQL logical CDC capability was verified in Area 02.
The Area 02 publication and replication slot were removed after testing.
Future CDC execution must establish its own controlled resources and evidence.

## AWS Boundary
AWS DMS recovery behavior, task checkpoints, retries, and replication health must be validated through actual AWS execution before being claimed.

## Implementation Boundary
Deduplication, idempotency, replay, late-event handling, and backfill implementation are intentionally delivered in their dedicated Areas.
This document defines the reliability requirements; it does not claim those implementations are complete.

## Claim Integrity
Reliability behavior must be supported by execution evidence when implemented.
Architecture documentation alone must not be represented as runtime validation.

## Change Control
Changes to reliability guarantees, recovery behavior, checkpoint semantics, or failure handling require documented impact assessment and validation.
