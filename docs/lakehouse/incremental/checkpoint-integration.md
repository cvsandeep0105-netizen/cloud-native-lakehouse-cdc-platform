# Incremental Batch and Checkpoint Integration

## Purpose
Area 22-B integrates the reusable incremental processing framework with a persistent local Iceberg checkpoint store.

## Checkpoint Contract
A checkpoint identifies the highest successfully processed source position for one source system, schema, and table.

## Batch Processing
Each batch is bounded by an inclusive source-position interval. On restart, processing begins at checkpoint_position + 1.

## Commit Boundary
The checkpoint is committed only after the incremental batch has been accepted. A failed downstream processing attempt must not advance the checkpoint.

## Idempotency
Duplicate deliveries are filtered by event_id before watermark/checkpoint advancement.

## Recovery
A restarted processor reloads the persisted checkpoint and resumes from the next source position.

## Monotonicity
Checkpoint regression is rejected. Persisted progress can only remain unchanged or advance.

## Storage
The validation uses a temporary local Iceberg checkpoint table. Production orchestration and durable operational recovery remain later Area 29–32 concerns.

## AWS Boundary
No AWS execution is claimed in Area 22-B.
