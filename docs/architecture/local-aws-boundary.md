# Project 02 — Local to AWS Architecture Boundary

## 1. Purpose

This document defines the boundary between locally implemented capabilities and AWS production-oriented capabilities.

The project will use local development to build and validate deterministic engineering behavior before AWS deployment. Local verification must not be presented as proof of AWS execution.

## 2. Local Development Layer

| Capability | Local Implementation | Purpose |
|---|---|---|
| Operational Database | PostgreSQL | Source-system modeling and CDC development |
| Processing | Apache Spark / PySpark | Distributed transformation development |
| Storage | Local filesystem / object-storage-compatible layout | Data lake development and testing |
| File Format | Apache Parquet | Columnar data processing |
| Lakehouse | Apache Iceberg | Table-format development and validation |
| CDC | Explicit CDC simulation/replay | Deterministic testing using static Olist data |
| Testing | Python / SQL test framework | Automated correctness validation |
| Configuration | Environment-based configuration | Local reproducibility |

## 3. AWS Target Layer

| Capability | AWS Candidate | AWS Verification Requirement |
|---|---|---|
| Object Storage | Amazon S3 | Actual AWS resource and access verification |
| Processing | AWS Glue / Spark | Actual job execution and evidence |
| CDC | AWS DMS | Actual task execution and CDC evidence |
| Catalog | AWS Glue Data Catalog | Actual catalog/table verification |
| Query | Amazon Athena | Actual query execution and metrics |
| Orchestration | AWS Step Functions | Actual workflow execution |
| Scheduling | Amazon EventBridge | Actual rule/trigger verification |
| Governance | AWS Lake Formation | Actual permissions/governance verification if deployed |
| Security | IAM / KMS / Secrets Manager | Actual policy/resource verification |
| Monitoring | Amazon CloudWatch | Actual logs/metrics verification |
| Infrastructure | Terraform | Actual plan/apply validation where deployed |

## 4. CDC Claim Boundary

The Olist source dataset is static historical data.

Any changes generated locally from Olist records are CDC simulation/replay and must be described that way.

A genuine CDC claim requires an actual operational source, CDC mechanism, change capture, downstream delivery, and verification of the resulting change events.

## 5. Evidence Levels

### Level 1 — Designed

The architecture or capability is documented but not implemented.

### Level 2 — Locally Verified

The capability has been implemented and tested in the local development environment.

### Level 3 — AWS Configuration Verified

AWS resources or configuration have been inspected and validated, but end-to-end runtime behavior may not yet have been demonstrated.

### Level 4 — AWS Execution Verified

The capability has actually executed in AWS and supporting evidence has been captured.

### Level 5 — Production Evidence

The capability has demonstrated production-oriented operational behavior under realistic workload, reliability, security, and performance conditions.

## 6. Portfolio Claim Rule

Final project documentation will label evidence according to these levels.

Local implementation will never be represented as AWS execution.

Architecture design will never be represented as deployment evidence.

Estimated cost will never be represented as observed AWS cost.

Simulated CDC will never be represented as genuine source-system CDC.

## 7. Migration Principle

The local implementation should remain structurally representative of the AWS target architecture where practical, while allowing implementation-specific differences required by managed AWS services.
