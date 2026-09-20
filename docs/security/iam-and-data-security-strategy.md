# IAM & Data Security Strategy

## Purpose

Define the security architecture for the Cloud-Native Lakehouse, CDC & AI-Ready Data Platform.

## Security Principles

- Least privilege
- Explicit authorization
- Separation of duties
- Defense in depth
- Credential minimization
- Encryption by default
- Auditable access
- Secure failure

## Identity Model

Human identities are separated from workload identities.

Production workloads use dedicated roles rather than shared human credentials.

Administrative access requires explicit authorization and must not be embedded in application code.

## AWS IAM Boundary

Production AWS roles are designed around the minimum permissions required for:

- S3 data access
- Glue catalog access
- Athena query access
- KMS encryption operations
- CloudWatch observability
- Orchestration services
- Data-processing workloads

No unrestricted administrator role is required by the data pipeline.

## S3 Security

Raw, Bronze, Silver, Gold, quarantine, and metadata areas require explicit access boundaries.

Raw data is immutable by policy. Write access is limited to controlled ingestion identities.

Production bucket policies must deny unintended public access.

## Catalog Security

Catalog metadata access is separated from unrestricted data mutation.

Production Glue Data Catalog permissions will be defined for the required databases, tables, and metadata operations only.

## PostgreSQL Security

Application identities must use dedicated credentials with only required database permissions.

Administrative PostgreSQL credentials are not stored in source code or committed configuration.

## Secrets Management

Secrets must be supplied through approved secret-management mechanisms or protected runtime configuration.

Credentials, tokens, private keys, and connection secrets must never be committed to Git.

## Encryption

Data at rest uses approved encryption mechanisms.

Production AWS data encryption will use AWS KMS-managed keys where appropriate.

Data in transit must use encrypted transport protocols where supported.

## Network Security

Production data services should operate inside explicitly controlled network boundaries.

Database access should be restricted to authorized workloads and administrative paths.

Public exposure of internal data services is prohibited unless explicitly required and secured.

## Auditability

Security-relevant access and administrative actions must be auditable.

Security events should correlate with pipeline run IDs, stage IDs, and incident IDs where applicable.

## Data Classification

Data classification must distinguish operational identifiers, transactional data, derived analytics, metadata, credentials, and security-sensitive configuration.

Credentials and security secrets are always treated as restricted.

## Local Development Boundary

Local development may use local PostgreSQL and local Iceberg storage.

Local credentials must remain outside source control.

Local implementation must not imply AWS production deployment.

## Security Failure Boundary

Security failures are blocking conditions. Processing must not continue by bypassing authentication, authorization, encryption, or governance controls.

## Human Control

Security policy changes require controlled human review.

AI-assisted capabilities cannot override deterministic security controls.

## AWS Boundary

This Area defines the AWS security architecture but does not execute AWS infrastructure changes.
