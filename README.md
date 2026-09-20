# Cloud-Native Lakehouse, CDC & AI-Ready Data Platform

[![Project Status](https://img.shields.io/badge/Status-Complete%20%2F%20Frozen-success)](https://github.com/cvsandeep0105-netizen/cloud-native-lakehouse-cdc-platform)
[![Platform](https://img.shields.io/badge/Platform-AWS-orange)](https://aws.amazon.com/)
[![Infrastructure](https://img.shields.io/badge/IaC-Terraform-7B42BC)](https://www.terraform.io/)
[![Lakehouse](https://img.shields.io/badge/Lakehouse-Apache%20Iceberg-blue)](https://iceberg.apache.org/)

## Project 02 — Cloud Data Engineering Platform

A production-oriented Data Engineering platform demonstrating cloud-native lakehouse architecture, operational PostgreSQL, CDC engineering, incremental processing, data quality, reconciliation, metadata, governance, security, observability, infrastructure as code, CI/CD, and bounded AI-assisted data engineering.

The primary engineering identity of this project is **Data Engineer**. AI is implemented as a bounded engineering capability rather than the primary platform identity.

## Engineering Objective

Transform realistic historical business data into a reliable, replayable, governed and analytics-ready data platform while separating locally validated behavior from actual AWS deployment evidence.

## Architecture

```text
Olist Historical Dataset
        |
        v
Operational PostgreSQL
        |
   +----+-------------------+
   |                        |
   v                        v
Initial Snapshot       Genuine Local CDC
   |                    PostgreSQL pgoutput
   +-----------+------------+
               |
               v
        Raw Immutable Layer
               |
               v
          Bronze Parquet
               |
               v
        Apache Iceberg
               |
               v
          Silver Layer
               |
               v
           Gold Layer
               |
       +-------+-------+
       |               |
       v               v
   Athena / SQL    AI-Ready Data

AWS foundation: S3 + KMS + Glue Catalog + Athena + IAM + CloudWatch + Terraform.

```

## What This Project Demonstrates

| Engineering Capability | Demonstration |
|---|---|
| Operational source | PostgreSQL |
| CDC | PostgreSQL logical decoding / pgoutput |
| Raw data | Immutable S3-backed deployment pattern |
| File format | Parquet |
| Lakehouse | Apache Iceberg Format V2 |
| Processing | Apache Spark / PySpark |
| Incremental processing | Checkpoint-bounded framework |
| Data quality | Deterministic validation framework |
| Reconciliation | Source-to-target trust controls |
| Metadata | Dataset, column and lineage registry |
| Orchestration | Dependency-gated pipeline stages |
| Recovery | Failure classes and recovery controls |
| Observability | Metrics, events and alert rules |
| Security | IAM, KMS, least privilege and secrets boundaries |
| Governance | Data contracts, lineage and compliance readiness |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| AI engineering | Bounded AI-assisted data engineering |

## Engineering Evidence

| Evidence | Result |
|---|---:|
| Automated engineering tests | **15/15 PASS** |
| Data quality checks | **63/63 PASS** |
| Reconciliation checks | **60/60 PASS** |
| Gold data products | **6** |
| Local Iceberg datasets | **9/9** |
| AWS Raw datasets | **9/9** |
| AWS Bronze datasets | **9/9** |
| Terraform drift | **No changes** |
| KMS key rotation | **Enabled** |
| Demo stages | **8/8 PASS** |

## CDC Engineering

The Olist dataset is static historical data and does not provide a live production CDC stream. Generated changes derived from that dataset are therefore treated explicitly as CDC simulation/replay.

Separately, genuine PostgreSQL logical decoding was validated locally using `pgoutput`, including controlled INSERT, UPDATE and DELETE capture, payload verification and LSN progression.

CDC engineering includes deterministic identity handling, ordering, deduplication, idempotency, replay, late-event handling, checkpoints and backfill controls.

## Lakehouse Engineering

The platform validates the following layered model:

```text
Raw → Bronze → Iceberg → Silver → Gold
```

Local Apache Iceberg validation covers 9/9 datasets, row-count reconciliation, column reconciliation and snapshot presence.

The AWS deployment does **not** claim AWS-native Iceberg tables. Local Iceberg execution and AWS object-storage deployment are intentionally separated in the evidence model.

## Gold Data Products

Six analytical products were designed and validated:

1. Order Performance
2. Customer Analytics
3. Product Performance
4. Seller Performance
5. Payment Analytics
6. Review Analytics

## Data Quality & Trust

The platform contains deterministic quality and reconciliation controls rather than treating successful pipeline execution as proof of data correctness.

- **63/63 Data Quality checks passed**
- **60/60 reconciliation checks passed**
- Source-to-target validation
- Schema and contract validation
- Incremental processing controls
- Failure and recovery controls

## Security & Governance

Security engineering includes least-privilege IAM design, KMS encryption, S3 public-access blocking, secrets boundaries, audit considerations, data contracts, metadata, lineage and compliance-readiness documentation.

No production credentials or secrets are stored in the repository.

## Infrastructure as Code

Terraform manages the AWS infrastructure foundation including S3, KMS, Glue Catalog, Athena, IAM and CloudWatch resources.

The final demo validates Terraform with `-detailed-exitcode` and requires the infrastructure to report no changes.

## CI/CD

GitHub Actions validates the engineering baseline, pinned Python dependencies, Terraform lockfile, secret-scan controls and automated tests.

## Performance & Scalability

The platform includes deterministic performance benchmarking and scalability evidence across increasing workloads. The benchmark evidence is retained under `evidence/` rather than presenting synthetic throughput as an AWS production SLA.

## AI Engineering Boundary

AI-assisted data engineering is deliberately bounded. Deterministic data quality, reconciliation, security and governance controls remain authoritative. Autonomous production mutation is disabled, and human review remains part of the control boundary.

## AWS Deployment Boundary

### Deployed and validated

- Amazon S3 data lake bucket
- S3 quarantine bucket
- AWS KMS key with rotation enabled
- AWS Glue Catalog database
- Amazon Athena workgroup
- IAM data-platform role
- CloudWatch log groups
- Terraform-managed infrastructure

### Evaluated but not claimed as deployed

- AWS DMS
- AWS Step Functions
- Amazon EventBridge
- AWS Secrets Manager
- AWS-native Iceberg table deployment

This distinction is intentional and documented as part of the project claim-integrity standard.

## Run the Project Demo

From the project root:

```powershell
.\scripts\demo.ps1
```

Expected result:

```text
PROJECT 02 DEMO STATUS: READY
```

The demo is designed as a safe interview/engineering validation workflow. It does not run `terraform apply`, destroy AWS resources, delete deployed data, or expose credentials.

## Engineering Runbook

[`docs/runbook/RUNBOOK.md`](docs/runbook/RUNBOOK.md)

## Engineering Report

[`Engineering Report`](docs/engineering-report/engineering-report.html)

The final report documents architecture, engineering decisions, evidence, security, governance, performance, cost engineering, AWS deployment, limitations and final acceptance.

## Repository Structure

```text
docs/                  Architecture, ADRs, runbook and engineering report
evidence/              Area-by-area engineering evidence
infrastructure/         Terraform infrastructure
scripts/                Validation and demo automation
src/                    Data engineering implementation
tests/                  Automated engineering tests
```

## Data Source

Olist Brazilian E-Commerce Public Dataset.

The dataset is static historical business data. Its use in this project is explicitly documented, including the distinction between historical replay/simulation and genuine local PostgreSQL CDC validation.

## Engineering Principles

- Correctness before technology quantity
- Deterministic and replayable processing
- Immutable source preservation
- Explicit incremental processing
- Data quality as a first-class control
- Idempotency and recovery as correctness requirements
- Least-privilege security
- Observable operations
- Evidence-backed engineering claims
- Clear separation between local validation and AWS execution

## Project Status

**Areas 01–39: Complete / Frozen**

**Area 40: Final portfolio integration, Engineering Report, acceptance and project freeze**

The project will be marked fully frozen only after the final README, Engineering Report, portfolio integration, GitHub validation and final acceptance are complete.

## Repository

https://github.com/cvsandeep0105-netizen/cloud-native-lakehouse-cdc-platform
