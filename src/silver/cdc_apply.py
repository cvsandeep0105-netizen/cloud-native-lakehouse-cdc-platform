from dataclasses import dataclass
from typing import Any, Dict, Iterable, List


@dataclass(frozen=True)
class CDCEvent:
    event_id: str
    operation: str
    source_position: int
    record_key: str
    record: Dict[str, Any]


class SilverCDCState:
    def __init__(self) -> None:
        self._records: Dict[str, Dict[str, Any]] = {}
        self._applied_events: set[str] = set()
        self._positions: Dict[str, int] = {}

    def apply(self, event: CDCEvent) -> str:
        if event.operation not in {'INSERT', 'UPDATE', 'DELETE'}:
            raise ValueError(f'Unsupported CDC operation: {event.operation}')

        if event.event_id in self._applied_events:
            return 'DUPLICATE_IGNORED'

        current_position = self._positions.get(event.record_key)
        if current_position is not None and event.source_position <= current_position:
            raise ValueError(
                f'Stale or out-of-order event for {event.record_key}: '
                f'{event.source_position} <= {current_position}'
            )

        if event.operation in {'INSERT', 'UPDATE'}:
            self._records[event.record_key] = dict(event.record)
        else:
            self._records.pop(event.record_key, None)

        self._positions[event.record_key] = event.source_position
        self._applied_events.add(event.event_id)
        return event.operation

    def get(self, record_key: str) -> Dict[str, Any] | None:
        record = self._records.get(record_key)
        return None if record is None else dict(record)

    def contains(self, record_key: str) -> bool:
        return record_key in self._records

    def applied_event_count(self) -> int:
        return len(self._applied_events)

    def record_count(self) -> int:
        return len(self._records)


def apply_events(events: Iterable[CDCEvent]) -> SilverCDCState:
    state = SilverCDCState()
    for event in events:
        state.apply(event)
    return state
