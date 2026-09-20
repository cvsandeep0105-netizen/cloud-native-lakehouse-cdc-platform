# Area 14 — CDC Idempotency Strategy

## Objective
Ensure repeated processing of the same CDC event produces the same resulting state as processing it once.

## Required Behavior
- First application of an event is accepted.
- Repeated application of the same event identity is recognized as already processed.
- Repeated application must not create duplicate downstream state.
- Processing state must be durable for production implementations.

## Idempotency Boundary
Idempotency is based on event identity, not only on the source row primary key.

## Failure Handling
If processing outcome is uncertain, the event must remain recoverable and must not be silently marked successful.
