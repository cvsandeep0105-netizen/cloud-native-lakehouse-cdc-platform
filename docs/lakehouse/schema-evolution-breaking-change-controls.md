# Area 23 - Breaking Schema Change Controls

## Purpose

Define mandatory controls for schema changes that can alter existing semantics, downstream compatibility, CDC interpretation, or technical identity.

## Data Type Changes

- Existing column meaning must remain unchanged.
- Widening or otherwise compatible changes require isolated validation.
- Potentially incompatible type changes require migration planning.
- Production type changes require documented compatibility evidence.

## Column Renames

- A rename is not treated as a simple additive change.
- Existing readers and CDC consumers must be assessed.
- Explicit old-name to new-name mapping is required.
- Production rollout requires dependency validation.

## Column Removal

- Column removal requires downstream dependency analysis.
- CDC consumers must be checked before removal.
- Historical readability must be considered.
- Removal requires an explicit migration and approval record.

## Primary Keys and Technical Identity

- Primary-key changes are architectural changes.
- Technical identity columns must not be regenerated or silently replaced.
- Key changes require explicit architectural review.
- Existing record identity must remain deterministic.

## CDC Contract Changes

- CDC event fields must retain their established semantics.
- Source position and checkpoint semantics must remain valid.
- Event ordering and idempotency guarantees must remain intact.
- Breaking CDC changes require coordinated source, event, Silver, and downstream migration.

## Production Gate

A breaking schema change cannot be applied to production solely because Iceberg accepts the DDL. Compatibility evidence, contract impact analysis, migration planning, and validation are required.

## Area 23-D Acceptance

- Data type change controls: PASS
- Column rename controls: PASS
- Column removal controls: PASS
- Primary-key and technical-identity controls: PASS
- CDC contract change controls: PASS
- Production migration gate: PASS

## Status

23-D: PASS
NEXT: AREA 23-E - Final Acceptance and Freeze
