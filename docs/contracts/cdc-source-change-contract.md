# Project 02 — CDC and Source-Change Contract Boundary

## Contract Status
Status: Draft — Area 09

## Source Change Boundary
The published Olist dataset is a static historical dataset.
It does not provide a native live CDC stream.

## Snapshot Contract
The initial operational load represents a source snapshot.
Snapshot records must preserve the source identifiers and source values.
Snapshot ingestion must be distinguishable from subsequent change-event processing.

## Change Event Contract
Any generated change stream derived from the historical Olist dataset is classified as CDC simulation or replay.
Change events must identify the source dataset and source record key.
Each event must contain an explicit operation type.
Supported operation types are INSERT, UPDATE, and DELETE.

## Operation Semantics
INSERT represents creation of a source record in the simulated change stream.
UPDATE represents a change to an existing source record.
DELETE represents removal of an existing source record.
Operation semantics must not be inferred from downstream state.

## Ordering Contract
Change-event processing must preserve a deterministic ordering attribute.
Ordering information must be retained with the event.
Equal or conflicting ordering values must be detected and handled explicitly.

## Event Metadata
Change events should carry sufficient metadata to support traceability, replay, and auditability.
Required metadata includes source dataset, source key, operation, event ordering information, and event timestamp or equivalent source-change time where available.

## Replay and Simulation Boundary
Historical CDC simulation is a controlled engineering mechanism for testing incremental processing.
Simulation must never be represented as production CDC from Olist.
Replay scenarios must be deterministic and repeatable.
Deduplication, idempotency, late events, replay, and backfill behavior will be engineered and validated in later Areas.

## Genuine Local CDC Boundary
Area 02 independently verified genuine PostgreSQL logical CDC using a controlled PostgreSQL test table, publication, replication slot, and pgoutput.
That evidence establishes local PostgreSQL CDC capability.
It does not establish live CDC capability from the published Olist files.

## AWS CDC Boundary
AWS DMS remains an architectural candidate for CDC.
AWS DMS execution, replication, or production CDC performance must not be claimed unless AWS runtime evidence is obtained.

## Contract Integrity
CDC events must preserve source identifiers and must not silently rewrite source values.
Invalid operations, missing keys, or unresolvable source records must be detected and reported.

## Change Control
Changes to CDC event structure, operation semantics, ordering rules, or source-change assumptions require documented impact assessment, validation, and approval.
