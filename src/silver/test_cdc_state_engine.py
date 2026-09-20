from src.silver.cdc_state_engine import SilverCDCEvent, SilverCDCStateEngine

event = SilverCDCEvent(
    event_id="E-TEST-001",
    source_system="postgresql",
    source_schema="project02",
    source_table="orders",
    transaction_id="TX-001",
    source_position="100",
    event_sequence="1",
    operation="INSERT",
    record_key="TEST-ORDER",
    event_timestamp=None,
    record={"order_id":"TEST-ORDER","order_status":"created"}
)

assert event.operation == "INSERT"
assert event.source_table == "orders"
engine = object.__new__(SilverCDCStateEngine)
assert engine.identity("orders") == ["order_id"]
assert engine.identity("order_items") == ["order_id", "order_item_id"]
assert engine.identity("order_payments") == ["order_id", "payment_sequential"]
assert engine.identity("order_reviews") == ["order_review_key"]
assert engine.identity("geolocation") == ["geolocation_id"]
assert engine.build_merge_condition("orders") == "t.order_id = s.order_id"
assert engine.build_merge_condition("order_items") == "t.order_id = s.order_id AND t.order_item_id = s.order_item_id"

print("21-BF: CDC STATE ENGINE CONTRACT PASS")
