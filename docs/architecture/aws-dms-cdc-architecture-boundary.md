# Project 02 — AWS DMS CDC Architecture Boundary

## Purpose
This document defines the architectural role and evidence boundary for AWS Database Migration Service (AWS DMS) within Project 02.

## Architectural Role
AWS DMS is an evaluated AWS option for source-to-target replication and CDC.
It may be used to replicate changes from a supported operational source into an AWS target such as Amazon S3.
The final implementation must be selected based on verified AWS requirements, source compatibility, target behavior, security, reliability, and cost.

## Logical AWS CDC Flow
Operational PostgreSQL source
? AWS DMS replication instance or equivalent managed replication infrastructure
? AWS DMS source endpoint
? AWS DMS CDC task
? Amazon S3 target
? Raw immutable data boundary
? downstream Bronze / Iceberg / Silver processing

## Snapshot and CDC
AWS DMS can conceptually support an initial full-load phase followed by ongoing CDC.
The initial full load establishes the target snapshot.
Subsequent changes are captured and delivered according to the configured CDC task behavior.
Project 02 must maintain a clear boundary between initial snapshot data and subsequent change events.

## Source Compatibility
The Project 02 operational source is local PostgreSQL.
Actual AWS DMS source compatibility, networking, authentication, replication settings, and task configuration must be validated in AWS before execution claims are made.

## Target Boundary
Amazon S3 is the planned AWS raw data-lake target.
Target object layout, partitioning, file format, transaction semantics, and downstream ingestion behavior require explicit validation during AWS execution.

## Security Architecture
AWS DMS connectivity must use least-privilege IAM and database permissions.
Secrets must be managed through approved secret-management mechanisms rather than source code or Git.
Network access must be restricted to the minimum required source and target paths.
Encryption in transit and at rest must be configured according to the AWS deployment design.

## Reliability Architecture
AWS DMS task state, checkpoints, retries, failures, latency, and replication health must be observable.
CDC recovery behavior must be validated rather than assumed.
Duplicate, replay, late-event, and partial-failure behavior must be handled by the downstream architecture where required.

## Evidence Boundary
Area 02 verified genuine PostgreSQL logical CDC locally.
Area 02 and Area 04 established AWS tooling availability and architectural evaluation.
No AWS DMS replication task has been executed or validated by this document.

## Explicit Non-Claims
The project does not currently claim:
- AWS DMS runtime execution
- AWS DMS replication throughput
- AWS DMS replication latency
- AWS DMS availability or recovery performance
- AWS DMS production cost
- AWS production CDC reliability

## Future AWS Validation
If AWS execution is later performed, evidence must include the relevant AWS configuration, task state, source/target connectivity, CDC activity, logs or metrics, validation results, and cost evidence where applicable.

## Claim Integrity
AWS DMS is an architectural candidate until actual AWS execution evidence exists.
Local PostgreSQL CDC verification must not be presented as AWS DMS verification.
