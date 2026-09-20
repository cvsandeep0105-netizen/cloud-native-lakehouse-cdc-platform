# Area 21-B — Silver Table & CDC State Model

## Purpose
Define the Silver analytical state and the metadata required to apply CDC changes safely and deterministically.

## Silver State
Each Silver table represents the latest governed business state reconstructed from the authoritative source snapshot plus valid CDC changes.

## Required CDC Metadata
Silver processing must retain technical metadata sufficient to establish provenance and processing state.

Required metadata:
- event_id — deterministic CDC event identity.
- operation — INSERT, UPDATE, or DELETE.
- source_position — authoritative source ordering position.
- event_timestamp — source event timestamp when available.
- processed_at — Silver processing timestamp.
- record_version — deterministic applied version or source position.

## State Rules
- INSERT creates the current record state.
- UPDATE replaces the affected attributes with the valid newer state.
- DELETE removes the current active state or records the deletion according to the table-specific retention contract.
- Older source positions must not overwrite newer applied state.
- Duplicate event identities must not create additional state changes.

## Initial Snapshot
The initial Silver state is derived from the validated Area 19 Iceberg snapshot before CDC changes are applied.

## CDC Application
CDC events are applied incrementally against the current Silver state using Areas 13–15 ordering, deduplication, idempotency, replay, and late-event controls.

## Referential Integrity
Silver processing must preserve the documented business relationships where the source contract requires them. A child change must not silently create an invalid authoritative relationship.

## Auditability
Technical CDC metadata must permit reconstruction of which source event produced the current Silver state.

## Schema Boundary
Business columns remain governed by the source and Iceberg contracts. CDC metadata is additive technical metadata and must not change the meaning of source business columns.

## Status
Area 21-B model: DEFINED
