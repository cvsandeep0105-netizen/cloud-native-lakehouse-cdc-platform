# Retry, Timeout & Dependency-Gate Policy

## Retry Policy

| Failure class | Retry | Checkpoint advance |
|---|---|---|
| Transient failure | Allowed | No |
| Checkpoint commit failure | Allowed | No |
| Schema failure | Not allowed | No |
| Blocking DQ failure | Not allowed | No |
| Reconciliation failure | Not allowed | No |
| Invalid CDC ordering | Not allowed | No |

Retries are permitted only for identified transient or checkpoint-commit failures. Retry must preserve idempotency and checkpoint controls.

## Timeout Policy

A stage timeout is treated as an unsuccessful stage execution. Dependent stages remain blocked until the timeout is investigated and the stage completes successfully.

For incremental processing, timeout must preserve the last committed checkpoint. Uncommitted work remains eligible for deterministic replay.

## Dependency-Gate Policy

- Upstream FAILED -> dependent BLOCKED
- Upstream RETRYING -> dependent remains BLOCKED
- Upstream SUCCEEDED -> dependent becomes eligible
- Upstream TIMEOUT -> dependent BLOCKED
- Blocking DQ failure -> downstream blocked
- Reconciliation failure -> downstream blocked

## Safety Rule

No retry, timeout handler, or dependency mechanism may bypass CDC ordering, deduplication, checkpoint, DQ, reconciliation, schema, security, or governance controls.

## Human Review

Schema failures, blocking DQ failures, reconciliation failures, invalid CDC ordering, and unresolved timeouts require human investigation before downstream progression.

## AWS Boundary

This policy is a logical orchestration control design. No AWS orchestration execution is claimed.
