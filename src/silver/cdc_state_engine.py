from dataclasses import dataclass
from typing import Any, Dict, List

from pyspark.sql import SparkSession

from src.silver.record_identity import RECORD_IDENTITY

@dataclass(frozen=True)
class SilverCDCEvent:
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

class SilverCDCStateEngine:
    ALLOWED_OPERATIONS = {"INSERT", "UPDATE", "DELETE"}

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def validate(self, event: SilverCDCEvent) -> None:
        if event.operation not in self.ALLOWED_OPERATIONS:
            raise ValueError(f"Unsupported CDC operation: {event.operation}")
        if event.source_table not in RECORD_IDENTITY:
            raise ValueError(f"Unsupported dataset: {event.source_table}")
        if not event.event_id:
            raise ValueError("event_id must not be empty")
        if not event.record_key:
            raise ValueError("record_key must not be empty")

    def already_applied(self, event_id: str, events_table: str) -> bool:
        safe = event_id.replace("'", "''")
        return self.spark.sql(
            f"SELECT COUNT(*) FROM {events_table} WHERE event_id = '{safe}'"
        ).first()[0] > 0

    def checkpoint(self, event: SilverCDCEvent, checkpoint_table: str):
        rows = self.spark.sql(
            f"""
            SELECT checkpoint_position
            FROM {checkpoint_table}
            WHERE source_system = '{event.source_system}'
              AND source_schema = '{event.source_schema}'
              AND source_table = '{event.source_table}'
            ORDER BY updated_at DESC
            LIMIT 1
            """
        ).collect()
        return rows[0][0] if rows else None

    def classify(self, event: SilverCDCEvent, events_table: str, checkpoint_table: str) -> str:
        self.validate(event)

        if self.already_applied(event.event_id, events_table):
            return "DUPLICATE_IGNORED"

        previous = self.checkpoint(event, checkpoint_table)
        if previous is not None and int(event.source_position) <= int(previous):
            raise ValueError(
                f"Stale CDC position: event={event.source_position}, checkpoint={previous}"
            )

        return event.operation

    def identity(self, dataset: str) -> List[str]:
        return list(RECORD_IDENTITY[dataset])

    def build_merge_condition(self, dataset: str, source_alias: str = "s", target_alias: str = "t") -> str:
        keys = self.identity(dataset)
        return " AND ".join(
            [f"{target_alias}.{key} = {source_alias}.{key}" for key in keys]
        )
