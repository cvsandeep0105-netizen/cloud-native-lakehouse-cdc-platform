# ADR-005 — CDC Architecture

- Status: Accepted
- Decision ID: ADR-005
- Scope: Change Data Capture and incremental change processing

## 1. Context

Project 02 uses the Olist Brazilian E-Commerce Public Dataset as its historical business dataset. The dataset is static and therefore does not itself provide a live production change stream.

The project nevertheless requires meaningful CDC engineering capabilities, including change identity, ordering, INSERT/UPDATE/DELETE semantics, deduplication, idempotency, replay, late-event handling, checkpointing, and backfill.

## 2. Requirements

- Preserve the distinction between historical source data and generated changes.
- Support deterministic CDC simulation/replay from static source data.
- Validate genuine relational-database CDC capability where technically practical.
- Support INSERT, UPDATE, and DELETE semantics.
- Support event identity and ordering.
- Support duplicate delivery testing.
- Support replay and recovery.
- Support late-event and backfill scenarios.
- Provide a credible AWS CDC path.
- Avoid making unsupported production CDC claims.

## 3. Options

### Option A — CDC Simulation / Replay

Generate deterministic change events from the static Olist dataset for development and testing.

Advantages:

- Fully reproducible.
- Deterministic.
- No external source-system dependency.
- Suitable for testing difficult event-ordering and replay scenarios.

Limitation:

- It is not genuine source-system CDC.

### Option B — PostgreSQL Logical Decoding

Use PostgreSQL logical decoding and the built-in pgoutput output plugin to validate genuine database change capture in a controlled local environment.

Advantages:

- Genuine database-level change capture.
- Relevant to relational CDC architecture.
- Provides a strong technical validation path.

Limitations:

- Requires PostgreSQL logical-decoding configuration.
- Requires a CDC consumer or replication client.
- Local validation does not prove AWS CDC execution.

### Option C — AWS DMS

Use AWS Database Migration Service for genuine database-to-S3 full-load and CDC execution when AWS deployment is performed.

Advantages:

- AWS-native managed CDC capability.
- Strong alignment with the target cloud architecture.
- Reduces custom CDC infrastructure.

Limitations:

- Requires AWS resources and configuration.
- Introduces AWS operational and cost considerations.
- Must be actually executed before making runtime claims.

## 4. Proposed Architecture

The project will use a layered CDC strategy:

1. Olist historical data provides the baseline business dataset.
2. PostgreSQL represents the operational relational source locally.
3. Deterministic CDC simulation/replay provides reproducible incremental-processing test data.
4. PostgreSQL logical decoding is used for a controlled genuine-CDC technical validation.
5. AWS DMS will be evaluated for genuine AWS CDC execution if AWS deployment is performed.
6. Downstream CDC processing will enforce identity, ordering, deduplication, idempotency, replay, late-event, and backfill controls.

## 5. Claim Integrity

CDC simulation will always be labeled as simulation/replay.

PostgreSQL logical-decoding results will be labeled as local CDC verification.

AWS DMS CDC will be labeled as AWS-verified only when the task has actually executed and evidence has been captured.

## 6. Current Decision Status

The layered CDC strategy is accepted for Project 02.

The local PostgreSQL CDC path has been technically validated using PostgreSQL logical decoding with the built-in pgoutput output plugin. A controlled test successfully captured INSERT, UPDATE, and DELETE changes from the operational database, and the resulting CDC payloads and LSN progression were verified.

AWS DMS remains the selected candidate for genuine AWS CDC execution if and when AWS deployment is performed. AWS DMS execution is not claimed by this decision because AWS deployment has not yet been performed.

Downstream deduplication, idempotency, replay, late-event handling, and backfill will be implemented and validated in their dedicated later project Areas rather than being claimed as complete by this architecture decision.

## 7. Consequences

This approach requires maintaining clear boundaries between simulation, local genuine CDC, and AWS genuine CDC.

In return, it provides reproducible testing while preserving technical honesty and allowing the project to demonstrate both CDC engineering fundamentals and cloud-native CDC architecture.
