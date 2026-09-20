# Project 02 — Silver CDC Persistent State Model

## Purpose
- Persist CDC processing state independently from the nine Silver business tables.
- Support restart recovery, deterministic replay, and idempotent event application.

## Control Tables
- silver_cdc_events: durable record of accepted CDC event identities and processing metadata.
- silver_cdc_checkpoints: durable source-position checkpoints for replay recovery.
- Silver business tables remain separate and are not replaced by control state.

## Event State
- event_id is the canonical Area 14 CDC event identity.
- source_position is the authoritative ordering position.
- operation records INSERT, UPDATE, or DELETE.
- source_system, source_schema, and source_table preserve source context.
- record_key identifies the governed business or technical source record.
- event_timestamp records source event time when available.
- processed_at records processing time.
- status records accepted processing state.

## Checkpoint State
- Checkpoints advance only after the corresponding CDC processing scope is successfully accepted.
- Replay resumes from events strictly greater than the persisted checkpoint.
- Checkpoint state must never be advanced past an uncommitted processing result.

## Idempotency
- event_id must be persisted before an event is considered safely reprocessable.
- A previously accepted event_id must be ignored on replay.
- In-memory state alone is insufficient for restart-safe processing.

## Record Ordering
- The latest accepted source_position governs record state.
- Older or equal source positions must not overwrite newer state.
- Area 13 ordering remains authoritative.

## Identity Special Cases
- order_reviews: review_id is retained but is not a sole unique key.
- geolocation: no reliable source primary key exists.
- Existing operational technical keys remain distinct from source identifiers.
- No new technical identity may silently replace source identity.

## Immutability Boundary
- Raw remains immutable.
- Bronze remains unchanged.
- Area 19 source Iceberg tables remain unchanged.
- Existing Silver snapshot tables are not destroyed or silently rebuilt by CDC-state initialization.

## Local/AWS Boundary
- Initial implementation is local Apache Iceberg.
- AWS execution is not claimed.
- AWS-native control-plane implementation remains a future deployment concern.

## Status
Draft — Area 21
