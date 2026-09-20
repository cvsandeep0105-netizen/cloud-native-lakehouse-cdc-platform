# Area 15 — CDC Replay Strategy

## Purpose
Define deterministic replay behavior for previously captured CDC events.

## Replay Principle
Replay must begin from a known checkpoint and process the captured source sequence deterministically.

## Requirements
- Replay uses preserved source event identity.
- Replay respects Area 13 source ordering.
- Area 14 idempotency prevents repeated application of the same event.
- Replay must not silently skip malformed events.
- Replay results must be auditable.

## Checkpoint
A replay checkpoint identifies the last successfully processed source position.

## Recovery
After failure, processing resumes from the last durable checkpoint rather than assuming all previously delivered events succeeded.

## Boundary
Replay is distinct from generating new source changes.
