# Project 02 — AWS Service Evaluation

## 1. Purpose

This document evaluates AWS services that may form the production architecture for Project 02.

Services will be selected based on demonstrated requirements and engineering fit rather than service popularity.

## 2. Storage — Amazon S3

### Requirements

- Durable object storage.
- Separation of raw, processed, quarantine, and audit data.
- Replayability.
- Encryption and access control.
- Integration with analytics and data-processing services.

### Evaluation

Amazon S3 is a strong candidate because the project requires an object-based data lake foundation with durable storage, scalable capacity, and integration with AWS analytics services.

### Key Considerations

- Bucket and prefix architecture.
- Encryption.
- IAM and data access policies.
- Lifecycle management.
- Immutable raw-data strategy.
- File layout and small-file management.

Status: Candidate — validation required.

## 3. Processing — AWS Glue / Apache Spark

### Requirements

- Distributed transformation.
- PySpark support.
- Parquet processing.
- Incremental processing.
- Lakehouse integration.
- AWS-native execution option.

### Evaluation

AWS Glue provides a managed Spark-based processing option and can reduce infrastructure-management requirements. Local Apache Spark / PySpark will provide a development and validation environment.

### Key Considerations

- Local-to-AWS compatibility.
- Startup overhead.
- Job sizing.
- Dependency management.
- Iceberg integration.
- Performance and cost.

Status: Candidate — validation required.

## 4. CDC — AWS DMS

### Requirements

- Initial full load.
- Ongoing CDC where a genuine source system is available.
- Change ordering.
- Delivery to the data lake.
- Encryption and operational monitoring.

### Evaluation

AWS DMS is a candidate for genuine database-to-S3 CDC execution because it supports full-load and CDC migration patterns. The project will separately maintain a local CDC simulation/replay path for deterministic development and testing against the static Olist dataset.

### Key Considerations

- Source database compatibility.
- CDC prerequisites.
- S3 target behavior.
- Event ordering.
- Operational monitoring.
- AWS execution cost.

Status: Candidate — AWS execution to be validated if deployed.

## 5. Lakehouse — Apache Iceberg

### Requirements

- Transactional table management.
- Incremental writes.
- Schema evolution.
- Snapshot-based table history.
- Analytics integration.

### Evaluation

Apache Iceberg is the leading lakehouse table-format candidate because the project requires reliable incremental table management and modern analytical access over object storage.

### Key Considerations

- Catalog integration.
- Merge/update/delete behavior.
- Partition evolution.
- Compaction.
- Snapshot retention.
- Athena and Spark compatibility.

Status: Candidate — technical validation required.

## 6. Catalog — AWS Glue Data Catalog

### Requirements

- Table metadata.
- Schema discovery.
- Integration with analytical services.
- Lakehouse metadata management.

### Evaluation

AWS Glue Data Catalog is a strong candidate for AWS-native metadata management and integration with Glue and Athena.

Status: Candidate — validation required.

## 7. Query — Amazon Athena

### Requirements

- SQL access to lakehouse data.
- Serverless analytical querying.
- Integration with S3 and the metadata/catalog layer.
- Query-cost visibility.

### Evaluation

Amazon Athena is a strong candidate for serverless SQL access to the lakehouse and for demonstrating query performance, partition pruning, and bytes-scanned cost behavior.

Status: Candidate — validation required.

## 8. Orchestration — AWS Step Functions

### Requirements

- Explicit workflow dependencies.
- Retry and failure handling.
- State visibility.
- Integration with AWS services.

### Evaluation

AWS Step Functions is a candidate for coordinating multi-stage workflows and representing explicit pipeline state without requiring a continuously running orchestration server.

Status: Candidate — validation required.

## 9. Scheduling — Amazon EventBridge

### Requirements

- Scheduled pipeline execution.
- Event-driven triggers.
- Integration with AWS workflows.

### Evaluation

Amazon EventBridge is a candidate for scheduled and event-driven workflow initiation.

Status: Candidate — validation required.

## 10. Governance — AWS Lake Formation

### Requirements

- Centralized data permissions.
- Fine-grained access control.
- Governance metadata.
- Analytics-service integration.

### Evaluation

AWS Lake Formation is a candidate for governance and fine-grained access control over the AWS data lake, subject to validating the required integration and operational complexity for this project.

Status: Candidate — validation required.

## 11. Security — IAM / KMS / Secrets Manager

### Requirements

- Least-privilege access.
- Encryption.
- Secure credential handling.
- Separation of responsibilities.

### Evaluation

IAM, AWS KMS, and AWS Secrets Manager form the primary security-service candidates for identity, encryption-key management, and secret storage.

Status: Candidate — validation required.

## 12. Observability — Amazon CloudWatch

### Requirements

- Logs.
- Metrics.
- Pipeline execution visibility.
- Operational alerting.

### Evaluation

Amazon CloudWatch is the primary AWS-native observability candidate for collecting service logs and metrics and supporting operational alerting.

Status: Candidate — validation required.

## 13. Infrastructure as Code — Terraform

### Requirements

- Reproducible infrastructure.
- Version-controlled infrastructure definitions.
- Reviewable changes.
- Deployment consistency.

### Evaluation

Terraform is a candidate for defining AWS infrastructure declaratively and maintaining infrastructure changes alongside application code.

Status: Candidate — validation required.

## 14. Evaluation Principle

Candidate status does not mean final selection.

Each major service will be accepted only after the relevant architecture, compatibility, security, performance, reliability, cost, and operational considerations have been evaluated.
