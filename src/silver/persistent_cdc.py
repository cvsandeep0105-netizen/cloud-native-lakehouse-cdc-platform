from dataclasses import dataclass
from typing import Any, Dict, Iterable, List

from pyspark.sql import SparkSession

from src.silver.config import ICEBERG_ROOT

@dataclass(frozen=True)
class PersistentCDCEvent:
    event_id: str
    source_system: str
    source_schema: str
    source_table: str
    transaction_id: str
    source_position: str
    event_sequence: str
    operation: str
    record_key: str
    event_timestamp: Any
    record: Dict[str, Any]

class PersistentCDCApplication:
    ALLOWED_OPERATIONS = {'INSERT', 'UPDATE', 'DELETE'}

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def event_exists(self, event_id: str) -> bool:
        row = self.spark.sql(
            "SELECT event_id FROM local.silver.silver_cdc_events WHERE event_id = " + repr(event_id) + " LIMIT 1"
        ).first()
        return row is not None

    def validate_event(self, event: PersistentCDCEvent) -> None:
        if event.operation not in self.ALLOWED_OPERATIONS:
            raise ValueError(f'Unsupported CDC operation: {event.operation}')
        if not event.event_id:
            raise ValueError('event_id must not be empty')
        if not event.source_table:
            raise ValueError('source_table must not be empty')
        if not event.record_key:
            raise ValueError('record_key must not be empty')

    def classify(self, event: PersistentCDCEvent) -> str:
        self.validate_event(event)
        if self.event_exists(event.event_id):
            return 'DUPLICATE_IGNORED'
        return event.operation

def validate_event_batch(events: Iterable[PersistentCDCEvent]) -> List[PersistentCDCEvent]:
    materialized = list(events)
    seen = set()
    for event in materialized:
        if event.operation not in PersistentCDCApplication.ALLOWED_OPERATIONS:
            raise ValueError(f'Unsupported CDC operation: {event.operation}')
        if event.event_id in seen:
            raise ValueError(f'Duplicate event_id within incoming batch: {event.event_id}')
        seen.add(event.event_id)
    return materialized
