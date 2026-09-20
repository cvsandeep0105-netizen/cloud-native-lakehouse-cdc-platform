# Area 16 — AWS S3 Data Lake Foundation

## Purpose
Establish the AWS S3 foundation and storage boundaries for the Project 02 cloud-native lakehouse.

## Primary Storage
Amazon S3 is the planned durable object-storage foundation for the Project 02 data lake.

## Logical Data Layers
- Raw: immutable source and CDC landing data.
- Bronze: standardized ingestion representation.
- Silver: validated and incrementally processed data.
- Gold: business-oriented analytical data products.

## Storage Principles
- Prefer immutable objects for raw ingestion.
- Separate data layers using explicit prefixes.
- Use deterministic object naming.
- Preserve source and ingestion metadata.
- Avoid uncontrolled overwrite of immutable raw data.
- Enable lifecycle and retention policies where appropriate.

## Security Principles
- Private buckets by default.
- Block public access.
- Least-privilege IAM.
- Encryption at rest.
- TLS for data in transit.
- No credentials stored in repository files.

## AWS Boundary
Actual AWS resource creation, configuration, execution, metrics, and cost observations are only claimed when independently verified.

## Local Boundary
Local development may emulate S3-compatible storage or validate object-layout behavior without representing an AWS deployment.

## Downstream Integration
S3 will provide the storage foundation for Raw, Bronze, Iceberg, Silver, and Gold processing in later areas.
