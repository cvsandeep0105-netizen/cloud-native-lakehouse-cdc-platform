from dataclasses import dataclass
from typing import Any, Dict

from pyspark.sql import SparkSession

from src.silver.record_identity import RECORD_IDENTITY

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
    record: Dict[str, Any]

class PersistentCDCError(Exception):
    pass

class PersistentSilverCDC:
    OPERATIONS = {"INSERT", "UPDATE", "DELETE"}

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def identity_columns(self, dataset: str):
        if dataset not in RECORD_IDENTITY:
            raise PersistentCDCError(f"Unsupported dataset: {dataset}")
        return tuple(RECORD_IDENTITY[dataset])

    def validate_event(self, event: PersistentCDCEvent):
        if event.operation not in self.OPERATIONS:
            raise PersistentCDCError(f"Unsupported operation: {event.operation}")
        if event.source_table not in RECORD_IDENTITY:
            raise PersistentCDCError(f"Unsupported source table: {event.source_table}")
        if not event.event_id:
            raise PersistentCDCError("event_id is required")
        if not event.record_key:
            raise PersistentCDCError("record_key is required")
        if not event.source_position:
            raise PersistentCDCError("source_position is required")

    def event_exists(self, events_table: str, event_id: str) -> bool:
        safe = event_id.replace(chr(39), chr(39) + chr(39))
        return self.spark.sql(
            f"SELECT COUNT(*) FROM {events_table} WHERE event_id = {chr(39)}{safe}{chr(39)}"
        ).first()[0] > 0

    def latest_checkpoint(self, checkpoint_table: str, event: PersistentCDCEvent):
        rows = self.spark.sql(
            f"""
            SELECT checkpoint_position
            FROM {checkpoint_table}
            WHERE source_system = {chr(39)}{event.source_system}{chr(39)}
              AND source_schema = {chr(39)}{event.source_schema}{chr(39)}
              AND source_table = {chr(39)}{event.source_table}{chr(39)}
            ORDER BY updated_at DESC
            LIMIT 1
            """
        ).collect()
        return rows[0][0] if rows else None

    def classify(self, event: PersistentCDCEvent, events_table: str, checkpoint_table: str):
        self.validate_event(event)

        if self.event_exists(events_table, event.event_id):
            return "DUPLICATE_IGNORED"

        checkpoint = self.latest_checkpoint(checkpoint_table, event)

        if checkpoint is not None and int(event.source_position) <= int(checkpoint):
            raise PersistentCDCError(
                f"Stale source position: event={event.source_position}, checkpoint={checkpoint}"
            )

        return event.operation

    def merge_condition(self, dataset: str):
        keys = self.identity_columns(dataset)
        return " AND ".join([f"t.{key} = s.{key}" for key in keys])

    def validate_record_identity(self, dataset: str, record: Dict[str, Any]):
        missing = [key for key in self.identity_columns(dataset) if key not in record]
        if missing:
            raise PersistentCDCError(
                f"Missing identity columns for {dataset}: {missing}"
            )

    def supported(self, dataset: str, operation: str) -> bool:
        return dataset in RECORD_IDENTITY and operation in self.OPERATIONS
