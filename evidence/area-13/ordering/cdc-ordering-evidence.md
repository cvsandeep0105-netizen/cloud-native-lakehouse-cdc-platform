# Area 13 — CDC Event Ordering Evidence

## Verified Stream
INSERT -> UPDATE -> DELETE -> COMMIT

## Observed Positions
- INSERT: 126
- UPDATE: 200
- DELETE: 232
- COMMIT: 295

## Result
All observed CDC message positions are strictly increasing.

## Ordering Authority
PostgreSQL logical decoding stream position is the authoritative ordering basis for genuine local PostgreSQL CDC.

## Boundaries
- Event timestamps are not the primary ordering authority.
- Cross-system global ordering is not claimed.
- Deduplication and idempotency are Area 14.
- Replay, late events, and backfill are Area 15.
