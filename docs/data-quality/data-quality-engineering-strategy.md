# Area 25 — Data Quality Engineering

## Purpose

Area 25 establishes the production-grade data quality engineering framework for Project 02.
The framework validates correctness, completeness, consistency, uniqueness, referential integrity, freshness, schema conformity, CDC integrity, and Gold business-metric quality.

## Quality Layers

1. Source and ingestion quality
2. Operational PostgreSQL quality
3. Raw immutable-layer integrity
4. Bronze structural and transformation quality
5. Silver CDC and record-state quality
6. Gold business-product quality
7. Cross-layer reconciliation quality

## Core Quality Dimensions

- Completeness
- Validity
- Uniqueness
- Referential integrity
- Consistency
- Accuracy and reconciliation
- Timeliness / freshness
- Schema conformity
- CDC ordering and checkpoint integrity
- Business-rule correctness

## Severity Model

- CRITICAL: pipeline must stop; trusted data cannot be published.
- HIGH: affected dataset/product must be quarantined or blocked.
- MEDIUM: pipeline may continue only under an explicit controlled policy.
- LOW: informational or non-blocking observation.

## Production Safety

- Existing production Raw, Bronze, Silver, and Gold data must not be modified by framework validation.
- Quality checks must be deterministic and reproducible.
- Failed checks must produce explicit evidence.
- No silent conversion of invalid data into valid-looking values.
- Quarantine is preferred over destructive deletion.

## Area 25 Boundary

Area 25 defines and implements data-quality engineering.
Reconciliation and trust controls are extended in Area 26.
Metadata, catalog, and lineage are handled in Area 27.

## Acceptance Gate

Area 25-A is complete when the quality dimensions, severity model, layer boundaries, failure policy, and production-safety rules are documented and reviewed.
