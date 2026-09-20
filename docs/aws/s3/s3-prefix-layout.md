# Area 16 — S3 Prefix Layout

## Root Layout
Project 02 uses a logical lakehouse prefix structure:

raw/
bronze/
silver/
gold/
quarantine/
metadata/
evidence/

## Raw
raw/ contains immutable source extracts and CDC landing objects.

## Bronze
bronze/ contains standardized representations produced from raw ingestion.

## Silver
silver/ contains validated, incrementally processed analytical data.

## Gold
gold/ contains business-oriented data products.

## Quarantine
quarantine/ contains records rejected by defined data-quality or contract controls.

## Metadata
metadata/ contains operational metadata, manifests, and processing information where appropriate.

## Evidence
evidence/ is reserved for project engineering evidence and is not treated as business data.
