from dataclasses import dataclass


@dataclass(frozen=True)
class ReplayEvent:
    event_id: str
    source_position: str


def validate_source_positions(events: list[ReplayEvent]) -> None:
    positions = [event.source_position for event in events]
    if positions != sorted(positions):
        raise ValueError('CDC replay events are not in source order')


def replay_from_checkpoint(events: list[ReplayEvent], checkpoint: str | None) -> list[ReplayEvent]:
    if checkpoint is None:
        return list(events)
    return [event for event in events if event.source_position > checkpoint]
