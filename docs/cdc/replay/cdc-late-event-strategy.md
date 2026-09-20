# Area 15 — Late Event Strategy

## Definition
A late event is an event received after processing has advanced beyond its source event position.

## Detection
Late status is determined using source ordering metadata such as WAL/LSN rather than arrival timestamp alone.

## Handling
- Detect the late event.
- Preserve the original source identity and position.
- Route it through the defined late-event processing path.
- Prevent silent loss.
- Preserve audit information.

## Boundary
Late-event handling must not redefine the authoritative source ordering.

## Idempotency
Area 14 event identity and idempotency rules continue to apply.
