# Area 13 — CDC Event Contract

## Purpose
Define the canonical contract for CDC events consumed by downstream Project 02 processing.

## Event Envelope
- event_id: unique identifier for the captured change event.
- source_system: originating operational source.
- source_schema: originating database schema.
- source_table: originating table.
- operation: INSERT, UPDATE, or DELETE.
- commit_lsn: PostgreSQL WAL commit position when available.
- transaction_id: source transaction identifier when available.
- event_timestamp: source event or commit timestamp when available.
- key: source business/technical key.
- before: previous row image when available.
- after: resulting row image when available.

## Operation Semantics
- INSERT represents creation of a source row.
- UPDATE represents a change to an existing source row.
- DELETE represents removal of a source row.

## Required Properties
- Events must preserve source identity.
- Events must preserve operation type.
- Events must retain source ordering metadata when available.
- Events must not silently change source meaning.
- Missing optional metadata must be represented explicitly rather than fabricated.

## Truth Boundary
This contract describes the CDC event model. It does not claim that the static Olist dataset provides native CDC.
