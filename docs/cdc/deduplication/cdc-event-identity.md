# Area 14 — CDC Event Identity

## Purpose
Define deterministic identity for CDC events so repeated delivery can be detected without changing source meaning.

## Identity Principle
A CDC event identity must be derived from stable source metadata and must not depend on arrival time.

## Preferred Identity Components
- source_system
- source_schema
- source_table
- source transaction identifier when available
- source WAL/LSN or equivalent source position when available
- transaction-local event sequence when available

## Identity Boundary
Event identity is distinct from the business primary key of the changed source row.

## Requirements
- The same captured source event must produce the same event identity.
- Two distinct source events must not intentionally share an identity.
- Arrival timestamp must not be used as the sole event identity.
- Missing source identity metadata must not be silently fabricated.
