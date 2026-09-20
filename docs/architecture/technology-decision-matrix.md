# Project 02 — Technology Decision Matrix

| Capability | Primary Candidate | Alternatives Considered | Decision Status |
|---|---|---|---|
| Operational Source | PostgreSQL | Aurora PostgreSQL, MySQL | To be validated |
| Object Storage | Amazon S3 | EFS, local filesystem | To be validated |
| Columnar File Format | Apache Parquet | ORC, CSV | To be validated |
| Lakehouse Table Format | Apache Iceberg | Delta Lake, Apache Hudi | To be validated |
| Distributed Processing | Apache Spark / PySpark | AWS Glue Spark, EMR Spark | To be validated |
| CDC | Local CDC simulation/replay + AWS DMS evaluation | Debezium, native database CDC | To be validated |
| Data Catalog | AWS Glue Data Catalog | Hive Metastore, Unity Catalog | To be validated |
| Analytical Query Engine | Amazon Athena | Trino, Redshift | To be validated |
| Orchestration | AWS Step Functions | Airflow/MWAA, Glue Workflows | To be validated |
| Event Scheduling | Amazon EventBridge | cron, Airflow scheduler | To be validated |
| Data Quality | Deterministic Python/SQL checks + AWS Glue Data Quality evaluation | Great Expectations, dbt tests | To be validated |
| Governance | AWS Lake Formation evaluation | Apache Ranger, catalog-only governance | To be validated |
| Encryption | AWS KMS | Application-managed encryption | To be validated |
| Secrets | AWS Secrets Manager | Environment variables, Parameter Store | To be validated |
| Monitoring | Amazon CloudWatch | Prometheus/Grafana, OpenTelemetry | To be validated |
| Infrastructure as Code | Terraform | AWS CDK, CloudFormation | To be validated |
| CI/CD | GitHub Actions | AWS CodePipeline/CodeBuild | To be validated |
| Local Containers | Docker | Native local installation | To be validated |

## Decision Rule

These are candidate technologies, not final claims.

Final selections will be made only after evaluating:

- Technical fit.
- AWS integration.
- Local development feasibility.
- Operational complexity.
- Reliability.
- Security.
- Performance.
- Cost.
- Testability.
- Maintainability.
- Portfolio relevance.

Where a managed AWS service is selected, the project will document what operational burden it removes and what trade-offs it introduces.

Where a local technology is used to simulate or represent an AWS capability, the documentation will explicitly identify it as a local implementation rather than claiming equivalent AWS execution.

## CDC Integrity Rule

The Olist dataset is historical and static. Any change stream generated from the dataset for development or testing will be explicitly described as CDC simulation/replay.

AWS DMS will be considered separately for genuine database-to-S3 CDC execution if AWS deployment is performed and verified.

## Finalization Rule

The matrix remains in a validation state until the relevant architecture decisions have been technically evaluated and documented.
