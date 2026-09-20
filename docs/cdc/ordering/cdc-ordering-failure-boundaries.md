# Area 13 — CDC Ordering Failure Boundaries

## Failure Conditions
- Missing WAL/LSN metadata.
- Invalid or non-monotonic source positions within a source stream.
- Broken transaction boundaries.
- Ambiguous event sequence.
- Cross-source ordering incorrectly assumed.

## Required Response
An ordering-contract violation must stop or quarantine the affected processing path rather than silently inventing ordering information.

## Recovery Boundary
Recovery and replay procedures are handled in Area 15. Idempotent reapplication is handled in Area 14.
