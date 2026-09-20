# Project 02 — Source-to-Change-Event Architecture

## Purpose
This document defines the logical flow from the operational source state to CDC change events and downstream consumers.

## Logical Flow
1. Olist historical source files are acquired as immutable source artifacts.
2. The Olist source is loaded into the project02 PostgreSQL operational representation.
3. The initial PostgreSQL state establishes the snapshot boundary.
4. Subsequent source changes are represented as change events.
5. Change events enter an immutable raw CDC boundary before downstream transformation.
6. Downstream processing consumes ordered change events for incremental state management.

## Historical Olist Simulation Path
Olist is a static historical dataset and therefore does not emit native live CDC events.
For historical testing, controlled changes may be generated from the Olist-derived operational state.
These events are classified as CDC simulation or replay.
The simulation must preserve source identifiers, operation type, ordering information, and relevant timestamps.

## Genuine PostgreSQL CDC Path
PostgreSQL logical replication provides the genuine local CDC mechanism.
Area 02 verified PostgreSQL logical CDC using wal_level=logical, a publication, a replication slot, pgoutput, and controlled INSERT, UPDATE, and DELETE operations.
That evidence establishes the local CDC capture capability.
The Area 02 test artifacts are retained under evidence/area-02/cdc.

## Snapshot Boundary
The snapshot is the initial state against which subsequent changes are applied.
CDC processing must not reapply the initial snapshot as change events.
The snapshot boundary must be recorded so that incremental processing has a deterministic starting point.

## Raw CDC Boundary
Captured or simulated change events must be preserved before transformation.
The raw boundary must retain source-level event information.
Raw events must be immutable and auditable.

## Event Envelope
A CDC event should contain, at minimum:
- source dataset
- source record key
- operation
- event ordering information
- event timestamp or equivalent source-change timestamp where available
- event payload or changed source values

## Downstream Consumers
CDC events will later feed Bronze, Iceberg, Silver, and Gold processing.
Deduplication, idempotency, late-event handling, replay, and backfill are intentionally deferred to their dedicated implementation Areas.

## AWS Architecture Boundary
AWS DMS may provide source-to-target CDC replication in an AWS implementation.
An AWS DMS design does not constitute AWS execution evidence.
AWS CDC runtime behavior will only be claimed after actual AWS validation.

## Failure Boundary
A failure during capture must not silently lose events.
Capture progress and downstream processing progress must be independently observable.
Failed or incomplete processing must be recoverable through checkpoints or equivalent mechanisms.

## Traceability
Every downstream record derived from CDC should remain traceable to its source dataset and source event information.

## Claim Integrity
Local PostgreSQL CDC is verified.
Olist historical change generation is simulation/replay.
AWS CDC execution is not claimed.
