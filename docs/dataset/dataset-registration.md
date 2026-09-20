# Project 02 — Dataset Registration

## Dataset Identity
- Name: Brazilian E-Commerce Public Dataset by Olist
- Publisher: Olist
- Distribution: Kaggle — olistbr/brazilian-ecommerce
- Historical period: 2016–2018
- Approximate order volume: 100,000 orders
- Core CSV files: 9

## Acquired Artifact
- Archive: data/raw/olist/brazilian-ecommerce.zip
- Extracted source boundary: data/raw/olist/extracted/
- Archive SHA-256: 967E41E04FC306FE604E2A693F488995A8B41E5047418F8A5C8E4ABD6DECA784

## Data Role
- Historical operational source for Project 02.
- PostgreSQL will represent the operational source.
- Initial snapshot ingestion will establish the baseline.
- Historical change scenarios derived from this static dataset will be classified as CDC simulation/replay.

## Immutability Boundary
- Acquired source files are preserved as immutable source evidence.
- Source files must not be edited in place.
- Transformations must write to downstream processing boundaries.
- Raw source data must not be committed to Git.

## Evidence
- Acquisition manifest: evidence/area-06/acquisition/dataset-manifest.md
- Archive and extracted-file SHA-256 values are recorded in the acquisition manifest.
