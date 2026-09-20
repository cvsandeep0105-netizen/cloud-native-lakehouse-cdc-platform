# Area 26 — Data Reconciliation & Trust Strategy

## Purpose

Area 26 establishes controls proving that data remains complete, consistent, traceable, and trustworthy as it moves through the Project 02 data platform.

## Reconciliation Boundaries

1. Source → Raw
2. Raw → Bronze
3. Bronze → Silver
4. Silver → Gold
5. CDC event → applied Silver state
6. Checkpoint → processed event boundary
7. Gold metric → authoritative Silver facts

## Reconciliation Types

- Row-count reconciliation
- Identity/key reconciliation
- Aggregate-value reconciliation
- Referential-integrity reconciliation
- CDC event reconciliation
- Checkpoint reconciliation
- Business-metric reconciliation
- Schema reconciliation

## Trust Principles

- Every reconciliation must have an authoritative source.
- Reconciliation must be deterministic and reproducible.
- Differences must never be silently ignored.
- Expected CDC mutations must be distinguished from unexplained discrepancies.
- Historical Iceberg physical files must not be confused with the current table state.
- A failed critical reconciliation blocks trusted publication.
- Evidence must preserve the observed values and acceptance decision.

## Discrepancy Classification

- EXPECTED: documented consequence of approved processing semantics.
- RECONCILED: difference explained by an approved transformation or CDC event.
- UNRESOLVED: difference without an accepted explanation.
- CRITICAL: discrepancy that invalidates downstream trust.

## Failure Policy

1. Detect discrepancy.
2. Identify authoritative source.
3. Quantify the difference.
4. Determine whether the difference is expected.
5. Preserve evidence.
6. Block publication when trust cannot be established.
7. Remediate only through controlled processing.

## Production Safety

- Reconciliation is read-only.
- No destructive correction is permitted during validation.
- Existing Raw, Bronze, Silver, and Gold data must remain unchanged.
- PostgreSQL must remain unchanged.
- AWS execution is not implied by local reconciliation.

## Area Boundary

Area 26 owns reconciliation and trust validation.
Data-quality rule definitions remain in Area 25.
Metadata, catalog, and lineage remain in Area 27.
