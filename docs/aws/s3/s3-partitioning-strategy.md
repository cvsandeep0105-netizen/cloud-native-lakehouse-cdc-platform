# Area 16 — S3 Partitioning Strategy

## Principle
Partitioning must improve data pruning and operational organization without creating excessive small partitions.

## Initial Partition Candidates
- ingestion_date
- source_table
- CDC operation where operationally justified

## Raw Layer
Raw ingestion is organized primarily by ingestion date and source domain/table.

## CDC
CDC landing data may use ingestion date while preserving source event position inside the event payload.

## Analytical Layers
Bronze, Silver, and Gold partitioning will be selected based on actual query and processing patterns in later areas.

## Small-File Boundary
Partition count and file size must be monitored before introducing additional partition dimensions.
