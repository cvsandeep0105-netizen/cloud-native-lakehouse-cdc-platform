# Area 13 — CDC Sequencing Rules

## Rules
- Every genuine PostgreSQL CDC event should retain its source WAL position where exposed by the capture mechanism.
- Commit boundaries must remain distinguishable.
- Transaction-local event sequence must not be replaced by wall-clock timestamp ordering.
- Events must be processed according to source sequence metadata before downstream state application.
- Missing sequence metadata must be treated as a contract violation for processing paths that require strict ordering.

## Determinism
Given the same captured CDC stream and the same starting checkpoint, event ordering must be reproducible.

## Scope Boundary
Deduplication, idempotency, replay, late-event handling, and backfill are separate concerns covered by Areas 14 and 15.
