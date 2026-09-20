# Area 25 — Data Quality Rule Catalog & Contracts

## Rule Governance

Each rule has a stable rule ID, quality dimension, scope, severity, acceptance condition, and failure action.
Rules are deterministic and must be independently reproducible.

## Source / Operational Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-SRC-001 | Completeness | Required source datasets exist | CRITICAL | Stop ingestion |
| DQ-SRC-002 | Schema | Expected source columns exist | CRITICAL | Stop ingestion |
| DQ-SRC-003 | Schema | Source column types are compatible | HIGH | Block affected dataset |
| DQ-SRC-004 | Uniqueness | Declared source identity is unique | HIGH | Quarantine affected records |
| DQ-SRC-005 | Referential Integrity | Declared source relationships resolve | HIGH | Block affected dataset |
| DQ-SRC-006 | Validity | Domain and range constraints hold | HIGH | Quarantine invalid records |

## Raw Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-RAW-001 | Completeness | Expected raw artifacts exist | CRITICAL | Stop downstream processing |
| DQ-RAW-002 | Integrity | Raw artifact checksum matches registered manifest | CRITICAL | Stop downstream processing |
| DQ-RAW-003 | Immutability | Previously accepted raw artifacts are not silently replaced | CRITICAL | Stop ingestion |

## Bronze Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-BRZ-001 | Completeness | Bronze dataset exists for every expected source dataset | CRITICAL | Block downstream processing |
| DQ-BRZ-002 | Reconciliation | Bronze row count reconciles with accepted input | HIGH | Block affected dataset |
| DQ-BRZ-003 | Schema | Bronze schema matches contract | HIGH | Block affected dataset |
| DQ-BRZ-004 | Transformation | Timestamp and nullable-integer normalization follows contract | HIGH | Block affected dataset |

## Silver Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-SLV-001 | Schema | Silver schema matches approved contract | CRITICAL | Block publication |
| DQ-SLV-002 | CDC Integrity | Event identity is deterministic | CRITICAL | Reject event |
| DQ-SLV-003 | CDC Integrity | Events at or before checkpoint are not re-applied | HIGH | Reject event |
| DQ-SLV-004 | CDC Ordering | Source positions are monotonic within the processing boundary | HIGH | Quarantine batch |
| DQ-SLV-005 | Idempotency | Duplicate event delivery does not create duplicate application | CRITICAL | Reject duplicate |
| DQ-SLV-006 | Referential Integrity | Required relationships remain valid | HIGH | Block affected dataset |

## Gold Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-GOLD-001 | Completeness | All required Gold products are available | CRITICAL | Block publication |
| DQ-GOLD-002 | Grain | Each Gold product maintains its declared grain | CRITICAL | Block publication |
| DQ-GOLD-003 | Reconciliation | Gold metrics reconcile with Silver source facts | CRITICAL | Block publication |
| DQ-GOLD-004 | Validity | Business metric domains are valid | HIGH | Block affected product |
| DQ-GOLD-005 | Uniqueness | Gold product identity is unique | CRITICAL | Block publication |
| DQ-GOLD-006 | Schema | Gold product columns match approved contract | CRITICAL | Block publication |

## Cross-Layer Rules

| Rule ID | Dimension | Rule | Severity | Failure Action |
|---|---|---|---|---|
| DQ-XLY-001 | Reconciliation | Source → Raw row/artifact reconciliation holds | HIGH | Block downstream |
| DQ-XLY-002 | Reconciliation | Raw → Bronze reconciliation holds | HIGH | Block downstream |
| DQ-XLY-003 | Reconciliation | Bronze → Silver reconciliation holds within defined CDC semantics | CRITICAL | Block publication |
| DQ-XLY-004 | Reconciliation | Silver → Gold business metrics reconcile | CRITICAL | Block publication |

## Threshold Policy

- CRITICAL rules require zero unresolved violations before trusted publication.
- HIGH rules require zero unresolved violations for the affected dataset or product.
- MEDIUM and LOW findings require explicit documented disposition.
- Thresholds must be dataset-specific where a universal threshold would be misleading.
- Threshold changes require controlled review and evidence.

## Failure Handling Contract

1. Detect.
2. Record rule ID and affected scope.
3. Prevent invalid data from being silently promoted.
4. Quarantine or reject according to severity.
5. Preserve evidence.
6. Permit controlled remediation and reprocessing.

## Boundary

This catalog defines DQ rules and acceptance contracts.
Operational reconciliation and trust controls are expanded in Area 26.
Metadata, catalog, and lineage controls remain in Area 27.
