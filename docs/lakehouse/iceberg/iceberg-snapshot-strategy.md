# Area 19 — Iceberg Snapshot Strategy

## Snapshot Principle
Iceberg table state is represented through immutable table snapshots and metadata transitions.

## Validation
Area 19 must prove that a created table has inspectable Iceberg metadata and a valid current snapshot after initial write.

## Historical State
Snapshot history is a table-format capability and is not equivalent to the CDC event history established in Areas 12–15.

## AWS Boundary
Local snapshot validation does not claim AWS-side Iceberg execution.
