import pytest
from src.incremental.framework import IncrementalEvent, IncrementalCheckpoint, IncrementalProcessor, IncrementalProcessingError

def event(event_id, position, table='orders', operation='INSERT'):
    return IncrementalEvent(event_id, 'postgresql', 'project02', table, position, operation)

def test_batch_creation_without_checkpoint():
    processor = IncrementalProcessor()
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-001')
    assert batch.start_position == 100
    assert batch.end_position == 200
    assert batch.batch_id == 'batch-001'

def test_checkpoint_advances_batch_start():
    checkpoint = IncrementalCheckpoint('postgresql','project02','orders',150)
    processor = IncrementalProcessor(checkpoint)
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-002')
    assert batch.start_position == 151

def test_select_events_filters_scope_and_range():
    processor = IncrementalProcessor()
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-003')
    events = [event('e1',120), event('e2',90), event('e3',180), event('e4',220), event('e5',130,'customers')]
    selected = processor.select_events(events,batch)
    assert [e.event_id for e in selected] == ['e1','e3']

def test_select_events_removes_duplicate_ids_and_sorts_deterministically():
    processor = IncrementalProcessor()
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-004')
    events = [event('z',150), event('a',150), event('z',150), event('b',120)]
    selected = processor.select_events(events,batch)
    assert [(e.source_position,e.event_id) for e in selected] == [(120,'b'),(150,'a'),(150,'z')]

def test_checkpoint_boundary_rejects_at_or_before_checkpoint():
    checkpoint = IncrementalCheckpoint('postgresql','project02','orders',150)
    processor = IncrementalProcessor(checkpoint)
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-005')
    assert batch.start_position == 151
    assert processor.select_events([event('e1',150)],batch) == []

def test_next_checkpoint_uses_max_event_position():
    processor = IncrementalProcessor()
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-006')
    checkpoint = processor.next_checkpoint(batch,[event('e1',120),event('e2',180),event('e3',150)])
    assert checkpoint.checkpoint_position == 180

def test_next_checkpoint_without_events_uses_previous_checkpoint():
    previous = IncrementalCheckpoint('postgresql','project02','orders',175)
    processor = IncrementalProcessor(previous)
    batch = processor.create_batch('postgresql','project02','orders',100,200,'batch-007')
    checkpoint = processor.next_checkpoint(batch,[])
    assert checkpoint.checkpoint_position == 175

def test_watermark_returns_max_position():
    processor = IncrementalProcessor()
    assert processor.watermark([event('e1',120),event('e2',190),event('e3',160)]) == 190

def test_watermark_returns_none_for_empty_events():
    processor = IncrementalProcessor()
    assert processor.watermark([]) is None

def test_batch_rejects_invalid_range():
    processor = IncrementalProcessor()
    with pytest.raises(ValueError):
        processor.create_batch('postgresql','project02','orders',200,100,'batch-008')
