from dataclasses import dataclass

@dataclass(frozen=True)
class IncrementalBatchConfig:
    source_system: str
    source_schema: str
    source_table: str
    start_position: int
    end_position: int
    batch_id: str

    def __post_init__(self):
        if not self.source_system:
            raise ValueError("source_system is required")
        if not self.source_schema:
            raise ValueError("source_schema is required")
        if not self.source_table:
            raise ValueError("source_table is required")
        if not self.batch_id:
            raise ValueError("batch_id is required")
        if self.start_position < 0:
            raise ValueError("start_position cannot be negative")
        if self.end_position < self.start_position:
            raise ValueError("end_position cannot be lower than start_position")
