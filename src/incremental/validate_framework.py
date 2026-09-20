from src.incremental.config import IncrementalBatchConfig
from src.incremental.framework import (
    IncrementalCheckpoint,
    IncrementalEvent,
    IncrementalProcessor,
    IncrementalProcessingError,
)

events = [
    IncrementalEvent("E100", "area22-test", "project02", "orders", 100, "INSERT"),
    IncrementalEvent("E101", "area22-test", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("E101", "area22-test", "project02", "orders", 110, "UPDATE"),
    IncrementalEvent("E102", "area22-test", "project02", "orders", 120, "DELETE"),
    IncrementalEvent("OTHER", "other-system", "project02", "orders", 130, "INSERT"),
    IncrementalEvent("FUTURE", "area22-test", "project02", "orders", 150, "INSERT"),
]

processor = IncrementalProcessor()
batch = processor.create_batch("area22-test", "project02", "orders", 100, 120, "AREA22-BATCH-001")
selected = processor.select_events(events, batch)

assert [event.event_id for event in selected] == ["E100", "E101", "E102"]
assert [event.source_position for event in selected] == [100, 110, 120]
assert processor.watermark(selected) == 120

checkpoint = processor.next_checkpoint(batch, selected)
assert checkpoint.checkpoint_position == 120

restart_processor = IncrementalProcessor(checkpoint)
restart_batch = restart_processor.create_batch("area22-test", "project02", "orders", 100, 150, "AREA22-BATCH-002")
assert restart_batch.start_position == 121

restart_events = restart_processor.select_events(events, restart_batch)
assert [event.event_id for event in restart_events] == ["FUTURE"]
assert restart_processor.watermark(restart_events) == 150

empty_restart = restart_processor.select_events(events, restart_batch)
assert [event.event_id for event in empty_restart] == ["FUTURE"]

try:
    IncrementalProcessor(IncrementalCheckpoint("area22-test", "project02", "orders", 120)).select_events(
        [IncrementalEvent("STALE", "area22-test", "project02", "orders", 120, "UPDATE")],
        IncrementalBatchConfig("area22-test", "project02", "orders", 120, 120, "AREA22-BATCH-STALE")
    )
except IncrementalProcessingError:
    pass
else:
    raise AssertionError("stale checkpoint event was not rejected")

assert IncrementalBatchConfig("x", "s", "t", 0, 0, "b").end_position == 0

print("22-A: BATCH BOUNDARY: PASS")
print("22-A: CHECKPOINT PROGRESSION: PASS")
print("22-A: WATERMARK CALCULATION: PASS")
print("22-A: DUPLICATE EVENT FILTERING: PASS")
print("22-A: RESTART/RESUME SEMANTICS: PASS")
print("22-A: STALE CHECKPOINT PROTECTION: PASS")
print("22-A: INCREMENTAL FRAMEWORK VALIDATION: PASS")
