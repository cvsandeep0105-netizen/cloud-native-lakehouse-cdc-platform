from src.incremental.framework import IncrementalCheckpoint, IncrementalProcessingError

class IcebergCheckpointStore:
    """Persistent checkpoint store backed by a local Iceberg table."""

    def __init__(self, spark, table_name):
        self.spark = spark
        self.table_name = table_name

    def create_table(self):
        self.spark.sql(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                source_system STRING,
                source_schema STRING,
                source_table STRING,
                checkpoint_position BIGINT,
                updated_at TIMESTAMP
            ) USING iceberg
        """)

    def read(self, source_system, source_schema, source_table):
        rows = self.spark.sql(f"""
            SELECT checkpoint_position
            FROM {self.table_name}
            WHERE source_system = "{source_system}"
              AND source_schema = "{source_schema}"
              AND source_table = "{source_table}"
            ORDER BY checkpoint_position DESC
            LIMIT 1
        """).collect()
        if not rows:
            return None
        return IncrementalCheckpoint(
            source_system=source_system,
            source_schema=source_schema,
            source_table=source_table,
            checkpoint_position=int(rows[0]["checkpoint_position"]),
        )

    def commit(self, checkpoint):
        current = self.read(
            checkpoint.source_system,
            checkpoint.source_schema,
            checkpoint.source_table,
        )

        if current is not None and checkpoint.checkpoint_position < current.checkpoint_position:
            raise IncrementalProcessingError(
                f"checkpoint regression: {checkpoint.checkpoint_position} < {current.checkpoint_position}"
            )

        self.spark.sql(f"""
            DELETE FROM {self.table_name}
            WHERE source_system = "{checkpoint.source_system}"
              AND source_schema = "{checkpoint.source_schema}"
              AND source_table = "{checkpoint.source_table}"
        """)

        self.spark.sql(f"""
            INSERT INTO {self.table_name}
            VALUES (
                "{checkpoint.source_system}",
                "{checkpoint.source_schema}",
                "{checkpoint.source_table}",
                {checkpoint.checkpoint_position},
                current_timestamp()
            )
        """)

        persisted = self.read(
            checkpoint.source_system,
            checkpoint.source_schema,
            checkpoint.source_table,
        )

        if persisted is None or persisted.checkpoint_position != checkpoint.checkpoint_position:
            raise IncrementalProcessingError("checkpoint persistence verification failed")

        return persisted
