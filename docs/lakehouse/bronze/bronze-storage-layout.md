# Area 18 — Bronze Storage Layout

## Root
data/lake/bronze/olist/

## Dataset Layout
Each Olist source dataset receives a dedicated Parquet dataset directory.

## Format
Apache Parquet.

## Partitioning
No artificial partitioning is introduced in Area 18 solely to demonstrate partitioning.

## Rationale
The Olist datasets are relatively small and heterogeneous. File-level dataset separation is more important than unnecessary partition fragmentation at this layer.

## Downstream
Silver processing may introduce additional physical optimization based on actual workload requirements.
