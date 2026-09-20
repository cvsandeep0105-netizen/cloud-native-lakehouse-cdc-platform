from dataclasses import dataclass
from typing import Iterable, List

from src.incremental.config import IncrementalBatchConfig

@dataclass(frozen=True)
class IncrementalEvent:
    event_id: str
    source_system: str
    source_schema: str
    source_table: str
    source_position: int
    operation: str

@dataclass(frozen=True)
class IncrementalCheckpoint:
    source_system: str
    source_schema: str
    source_table: str
    checkpoint_position: int

class IncrementalProcessingError(Exception):
    pass

class IncrementalProcessor:
    """Deterministic checkpoint-bounded incremental processing boundary."""

    def __init__(self, checkpoint: IncrementalCheckpoint | None = None):
        self.checkpoint = checkpoint

    def create_batch(self, source_system: str, source_schema: str, source_table: str,
                    start_position: int, end_position: int, batch_id: str):
        if self.checkpoint is not None:
            if (self.checkpoint.source_system == source_system
                    and self.checkpoint.source_schema == source_schema
                    and self.checkpoint.source_table == source_table
                    and start_position <= self.checkpoint.checkpoint_position):
                start_position = self.checkpoint.checkpoint_position + 1
        return IncrementalBatchConfig(
            source_system=source_system,
            source_schema=source_schema,
            source_table=source_table,
            start_position=start_position,
            end_position=end_position,
            batch_id=batch_id,
        )

    def select_events(self, events: Iterable[IncrementalEvent], batch: IncrementalBatchConfig) -> List[IncrementalEvent]:
        selected = []
        seen_ids = set()

        for event in events:
            if event.source_system != batch.source_system:
                continue
            if event.source_schema != batch.source_schema:
                continue
            if event.source_table != batch.source_table:
                continue
            if not (batch.start_position <= event.source_position <= batch.end_position):
                continue
            if event.event_id in seen_ids:
                continue
            seen_ids.add(event.event_id)
            selected.append(event)

        selected.sort(key=lambda item: (item.source_position, item.event_id))

        if selected and self.checkpoint is not None:
            if (self.checkpoint.source_system == batch.source_system
                    and self.checkpoint.source_schema == batch.source_schema
                    and self.checkpoint.source_table == batch.source_table
                    and selected[0].source_position <= self.checkpoint.checkpoint_position):
                raise IncrementalProcessingError("selected event is at or before checkpoint")

        return selected

    def next_checkpoint(self, batch: IncrementalBatchConfig, events: Iterable[IncrementalEvent]) -> IncrementalCheckpoint:
        positions = [event.source_position for event in events]
        if not positions:
            if self.checkpoint is not None:
                return self.checkpoint
            return IncrementalCheckpoint(
                source_system=batch.source_system,
                source_schema=batch.source_schema,
                source_table=batch.source_table,
                checkpoint_position=batch.start_position - 1,
            )

        return IncrementalCheckpoint(
            source_system=batch.source_system,
            source_schema=batch.source_schema,
            source_table=batch.source_table,
            checkpoint_position=max(positions),
        )

    def watermark(self, events: Iterable[IncrementalEvent]) -> int | None:
        positions = [event.source_position for event in events]
        return max(positions) if positions else None
