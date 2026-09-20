import pytest
from src.cdc.deduplication import build_event_identity, deduplicate_event_ids, apply_idempotently

def test_build_event_identity_is_deterministic():
    a = build_event_identity('postgresql','project02','orders','tx1','100','1')
    b = build_event_identity('postgresql','project02','orders','tx1','100','1')
    assert a == b
    assert len(a) == 64

def test_build_event_identity_changes_when_identity_component_changes():
    a = build_event_identity('postgresql','project02','orders','tx1','100','1')
    b = build_event_identity('postgresql','project02','orders','tx1','101','1')
    assert a != b

def test_build_event_identity_rejects_missing_component():
    with pytest.raises(ValueError):
        build_event_identity('postgresql','project02','orders','tx1','','1')

def test_deduplicate_event_ids_preserves_first_seen_order():
    assert deduplicate_event_ids(['a','b','a','c','b','c']) == ['a','b','c']

def test_apply_idempotently_accepts_once_and_rejects_repeat():
    processed = set()
    assert apply_idempotently(processed, 'event-1') is True
    assert apply_idempotently(processed, 'event-1') is False
    assert processed == {'event-1'}
