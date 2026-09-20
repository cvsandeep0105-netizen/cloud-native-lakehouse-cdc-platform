# Project 02 — Silver CDC Persistent Table Contract

## silver_cdc_events
- event_id: string, canonical Area 14 event identity, required, unique processing identity.
- source_system: string, required.
- source_schema: string, required.
- source_table: string, required.
- transaction_id: string, required.
- source_position: string, required, authoritative source ordering value.
- event_sequence: string, required.
- operation: string, required, one of INSERT, UPDATE, DELETE.
- record_key: string, required, deterministic identity of the affected record.
- event_timestamp: timestamp, nullable when unavailable from the source event.
- processed_at: timestamp, required.
- status: string, required, accepted processing state.

## silver_cdc_checkpoints
- source_system: string, required.
- source_schema: string, required.
- source_table: string, required.
- checkpoint_position: string, required.
- updated_at: timestamp, required.
- status: string, required.

## Constraints
- event_id is the durable idempotency key.
- The combination of source context and event identity must remain traceable.
- source_position must be retained exactly as received.
- operation values outside INSERT, UPDATE, DELETE are invalid.
- record_key must be deterministic and must not silently replace source identifiers.
- Checkpoints advance only after successful processing.

## Storage
- Both control tables use Apache Iceberg.
- Control tables are separate from Silver business-state tables.
- Local Hadoop catalog is used for the current implementation.
- AWS deployment is not claimed.

## Immutability
- Existing Raw, Bronze, Area 19 Iceberg source tables, and initial Silver snapshot tables must not be altered during control-table initialization.

## Status
Draft — Area 21
