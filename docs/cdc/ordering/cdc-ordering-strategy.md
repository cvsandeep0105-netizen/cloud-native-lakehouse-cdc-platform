# Area 13 — CDC Ordering Strategy

## Ordering Authority
PostgreSQL WAL/LSN and transaction boundaries are the authoritative ordering metadata for genuine local PostgreSQL CDC.

## Ordering Levels
1. WAL/LSN ordering establishes source-log position.
2. Transaction ordering groups changes committed by the same source transaction.
3. In-transaction ordering is preserved according to the logical-decoding event sequence.
4. Event timestamps are informational and are not the primary ordering authority.

## Cross-Source Boundary
Ordering guarantees are source-specific. Events from independent source systems must not be assumed to have a globally comparable order without an explicit coordination mechanism.

## Late Events
An event with an older source position received later is treated as late-arriving data. Handling is deferred to Area 15.

## Duplicate Events
Ordering metadata may participate in deterministic event identity, but duplicate prevention and idempotency are deferred to Area 14.
