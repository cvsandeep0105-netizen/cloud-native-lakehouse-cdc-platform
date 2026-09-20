# IAM Role & Permission Model

## Purpose

Define explicit IAM identities and minimum permission boundaries for the Project 02 AWS architecture.

## Role Model

| Role | Purpose | Access Boundary |
|---|---|---|
| DataIngestionRole | Controlled raw-data ingestion | Raw S3 write and required metadata operations |
| DataProcessingRole | Bronze/Silver/Gold processing | Required S3 data paths and catalog operations |
| OrchestrationRole | Pipeline orchestration | Required workflow invocation and state operations |
| QueryRole | Analytical querying | Read-only Gold/catalog access |
| ObservabilityRole | Monitoring and operational visibility | CloudWatch/log read access |
| SecurityAuditRole | Security verification | Read-only security and audit visibility |
| DeploymentRole | Controlled infrastructure deployment | Explicit IaC-managed resource permissions |
| HumanDeveloperRole | Development and investigation | Non-production and explicitly approved access |

## Least-Privilege Rules

- No pipeline workload receives unrestricted AdministratorAccess.
- Each workload receives only the services and resources required for its function.
- Resource-level restrictions should be used wherever practical.
- Read and write permissions are separated where operationally possible.
- Production access is separated from development access.
- Security administration is separated from application processing.

## S3 Permission Boundaries

DataIngestionRole:
- Write to approved Raw prefixes.
- Read only the source configuration required for ingestion.
- No unrestricted deletion permission.

DataProcessingRole:
- Read required Raw/Bronze/Silver inputs.
- Write only approved Bronze/Silver/Gold destinations.
- No permission to modify IAM.

QueryRole:
- Read-only access to approved Gold data.
- No write or delete access.

## Catalog Permission Boundaries

Catalog permissions must be limited to required databases and tables.

Processing workloads may create or update metadata only where required by the pipeline design.

Query workloads receive metadata read access without data mutation permissions.

## KMS Permission Boundaries

Encryption keys must not be broadly usable by every workload.

Encryption and decryption permissions are granted only to identities requiring those operations.

Key administration is separated from normal data-processing permissions.

## Orchestration Boundary

OrchestrationRole may invoke approved pipeline components and record execution state.

It must not receive unrestricted access to unrelated data or security services.

## Observability Boundary

ObservabilityRole is read-oriented.

It may inspect approved logs, metrics, alarms, and operational evidence without modifying production data.

## Human Access

Human identities must use individually attributable credentials.

Shared human credentials are prohibited.

Privileged operations require explicit authorization and auditing.

## Explicitly Prohibited

- Hard-coded AWS credentials
- Long-lived credentials embedded in source code
- Wildcard administrative permissions without documented justification
- Public S3 data access
- Cross-environment access without authorization
- AI-driven IAM policy mutation

## Deployment Status

This document defines the intended IAM model only.

No AWS IAM roles or policies are created or modified in Area 33-B.
