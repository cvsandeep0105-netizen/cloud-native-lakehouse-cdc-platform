# Area 15 — CDC Replay Checkpoint Strategy

## Checkpoint Model
A checkpoint records the highest source position successfully committed by the downstream processing path.

## Required Properties
- Checkpoints must be durable in production implementations.
- A checkpoint advances only after successful processing.
- Failed processing must not advance the checkpoint.
- Reprocessing from an earlier checkpoint must remain safe through Area 14 idempotency.

## Recovery Rule
Restart from the last confirmed checkpoint and replay subsequent source events in authoritative order.

## Determinism
The same source event sequence and starting checkpoint must produce reproducible processing behavior.
