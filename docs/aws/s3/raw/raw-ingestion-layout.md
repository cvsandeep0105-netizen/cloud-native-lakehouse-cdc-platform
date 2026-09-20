# Area 17 — Raw Ingestion Layout

## Logical Structure
raw/olist/{table}/
raw/cdc/{source_table}/

## Olist
Original Olist source artifacts are organized under the Olist raw domain.

## CDC
CDC landing artifacts are organized separately from static source artifacts.

## Metadata
Ingestion metadata must identify source, ingestion execution, object identity, and acquisition context.

## Immutability
Existing raw artifacts must not be overwritten by ordinary ingestion.
