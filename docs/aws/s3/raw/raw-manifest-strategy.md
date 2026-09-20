# Area 17 — Raw Manifest Strategy

## Purpose
Track raw ingestion artifacts and establish reproducibility.

## Manifest Fields
- source_system
- source_dataset
- source_table
- ingestion_identifier
- object_path
- file_size
- checksum
- ingestion_timestamp
- source_license_or_usage_reference

## Integrity
Checksums provide a deterministic mechanism for detecting unexpected raw-object changes.

## Boundary
Manifest metadata describes ingestion artifacts and does not replace source data contracts.
