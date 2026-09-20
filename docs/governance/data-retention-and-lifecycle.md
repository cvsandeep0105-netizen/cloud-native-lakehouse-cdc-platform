# Data Retention & Lifecycle

## Lifecycle

Source → Raw → Bronze → Silver → Gold → Archive / Deletion

## Controls
- Retention requirements must be defined by data class.
- Raw data lifecycle must be controlled.
- Derived analytical products require documented retention.
- Archive processes must be authorized.
- Deletion must be deterministic and auditable.
- Deletion must respect applicable legal, contractual, and operational requirements.
- Retention-policy changes require controlled approval.

## Deletion Safety

Deletion must never be performed merely to resolve a processing failure.

Production deletion requires explicit authorization and evidence.

## Boundary

No production data is deleted or modified by Area 34.
