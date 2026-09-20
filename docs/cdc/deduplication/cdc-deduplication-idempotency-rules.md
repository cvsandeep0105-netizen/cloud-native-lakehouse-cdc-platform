# Area 14 — Deduplication & Idempotency Rules

## Rules
- Event identity must be deterministic.
- Duplicate events must be detectable.
- The same event must be safe to process repeatedly.
- Distinct events for the same source key must remain distinguishable.
- Source ordering must remain authoritative for ordered application.
- Arrival order must not redefine source event identity.
- Failed processing must not be treated as successful processing.
- Deduplication state must be auditable.

## Deferred Scope
Replay, late-arriving events, and backfill are handled in Area 15.
