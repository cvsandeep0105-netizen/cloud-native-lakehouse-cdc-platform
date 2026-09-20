# Project 02 — Cloud-Native Lakehouse, CDC & AI-Ready Data Platform on AWS

## 1. Executive Summary

Project 02 is a production-oriented Data Engineering platform demonstrating cloud data platform engineering, CDC, lakehouse architecture, incremental processing, data quality, governance, security, observability, Infrastructure as Code, CI/CD, performance engineering, cost engineering, and bounded AI-assisted data engineering.

Primary identity: Data Engineer. Specialization: Cloud Data Platforms, CDC/Streaming, Lakehouse Engineering, and AI-enabled Data Systems.

## 2. Data Source

The platform uses the Olist Brazilian E-Commerce Public Dataset. The historical dataset is static. Generated historical changes are treated as CDC simulation/replay. Genuine PostgreSQL logical CDC was independently validated locally using PostgreSQL logical decoding and pgoutput.

## 3. Architecture

The platform follows a Raw → Bronze → Silver → Gold lakehouse progression. PostgreSQL provides the operational relational source. Snapshot and CDC boundaries feed immutable/raw processing, Bronze Parquet, Apache Iceberg, Silver incremental processing, and Gold business data products.

## 4. Lakehouse

The local lakehouse contains 9 Apache Iceberg Format V2 tables. Apache Iceberg 1.11.0 and Spark 3.5.8 were validated. The tables cover customers, geolocation, orders, order items, payments, reviews, products, sellers, and category translation.

## 5. CDC Engineering

The project validates logical CDC capture, event ordering, deterministic identity, deduplication, idempotent processing, replay, checkpoint recovery, late-event handling, and backfill boundaries. Local PostgreSQL CDC evidence uses pgoutput. AWS DMS is documented as an architecture option and is not claimed as deployed.

## 6. Data Quality and Reconciliation

Data profiling, source contracts, schema controls, key/relationship validation, deterministic data-quality rules, reconciliation, metadata, lineage, and business metric trust were implemented before AWS deployment.

## 7. Gold Data Products

Six business data products were implemented: Order Performance, Customer Analytics, Product Performance, Seller Performance, Payment Analytics, and Review Analytics.

## 8. AI Engineering Boundary

AI is a bounded engineering capability rather than the primary project identity. Deterministic controls remain authoritative. AI-assisted recommendations require human review, and autonomous production mutation is disabled.

## 9. Orchestration, Recovery and Observability

The project includes dependency-gated orchestration, checkpoint/restart behavior, failure taxonomy, recovery controls, operational runbooks, SLO/SLA targets, structured observability, alert scenarios, and recovery integration.

## 10. Security and Governance

Security engineering covers IAM, least privilege, secrets boundaries, encryption, KMS, network/data-access controls, audit monitoring, data classification, retention, lineage, governance, and compliance readiness. Formal certification is not claimed.

## 11. Infrastructure as Code

Terraform manages the AWS infrastructure boundary, including S3, KMS, Glue Catalog, Athena, IAM, and CloudWatch resources. Post-deployment Terraform validation reported no configuration drift.

## 12. CI/CD and Supply Chain

GitHub Actions validates Python compilation, pytest, Terraform formatting/initialization/validation, and secret-pattern controls. Dependencies and Terraform provider versions are pinned/locked where applicable.

## 13. Performance and Scalability

CDC processing benchmarks and scalability tests were completed locally across 100k, 200k, 500k, and 1m synthetic events. Correctness remained true across the tested workloads. The benchmark evidence is retained under evidence/area-37/.

## 14. Cost Engineering

AWS pricing inputs, workload assumptions, scenario analysis, optimization controls, monitoring expectations, and architecture review were documented. Actual AWS billing spend is not represented as an observed project metric unless directly evidenced.

## 15. AWS Deployment

AWS account environment: ap-south-1 (Mumbai).

Verified infrastructure includes the S3 data lake, S3 quarantine bucket, KMS customer-managed key, Glue Catalog database, Athena workgroup, IAM role/policy, and CloudWatch log groups.

Raw deployment: 9/9 Olist CSV objects verified.

Bronze deployment: 9/9 Parquet datasets verified.

S3 encryption uses AWS KMS. S3 public access blocking and versioning were verified. KMS rotation is enabled. Terraform post-deployment plan reported no changes.

## 16. Evidence and Claim Integrity

The project explicitly separates local validation, AWS configuration, AWS execution evidence, and production-style evidence. Local execution is not represented as AWS execution. Architecture candidates are not represented as deployed services without direct evidence.

The authoritative Area 40 evidence index is stored at evidence/area-40-final-evidence-index.json.

## 17. Area Completion

Areas 01–39 are complete and frozen. Area 40 is the final portfolio integration, Engineering Report, acceptance, and project freeze stage.

## 18. Limitations

The Olist source is historical rather than a live production source. AWS DMS, Step Functions, EventBridge, Secrets Manager, and other candidate services are not claimed as deployed unless directly evidenced. Formal regulatory certification and contractual AWS SLA claims are not made.

## 19. Final Acceptance

Final acceptance requires reconciliation of technical evidence, GitHub presentation, Engineering Report publication, portfolio integration, and final project freeze under Area 40.

---

Project 02 — Cloud-Native Lakehouse, CDC & AI-Ready Data Platform on AWS
