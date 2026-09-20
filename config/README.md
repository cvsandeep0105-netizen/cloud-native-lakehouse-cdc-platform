# Project 02 — Configuration Contract

## Purpose
Defines the configuration boundary for local development and future AWS execution.

## Configuration Principles
- Application code must not contain environment-specific secrets or credentials.
- Configuration values must be explicit and documented.
- Secrets must be supplied through secure mechanisms and never committed.
- Local development and AWS execution must remain distinguishable.

## Configuration Categories
### Runtime
Python runtime, Spark settings, logging level, and execution mode.

### Source Database
PostgreSQL host, port, database, schema, and non-secret connection settings.

### Data Lake
S3 bucket, AWS region, prefixes, and storage-layer configuration.

### Processing
Spark execution settings, batch/incremental parameters, checkpoints, and data-quality thresholds.

### AWS
AWS region, account context, service configuration, and execution-specific settings.

### Secrets
Database passwords, access credentials, tokens, and other sensitive values must be supplied externally and must never be stored in Git.

## Environment Separation
- Local configuration is used for local development and validation.
- AWS configuration is introduced only when AWS execution is intentionally performed.
- AWS execution evidence must be recorded separately from local validation evidence.

## Secret Handling
- Never commit .env files containing secrets.
- Never place secrets in source code, documentation examples, tests, logs, or command history where avoidable.
- Use AWS Secrets Manager or an equivalent approved secret-management mechanism for AWS workloads.

## Naming Convention
Configuration names should use uppercase environment-variable style names with a consistent PROJECT02_ prefix where environment variables are introduced.

## Current Boundary
No production credentials or AWS service credentials are configured for Project 02 at this stage.
AWS CLI and boto3 availability do not constitute AWS execution.

## Change Control
Configuration changes must be reviewed for scope, security impact, reproducibility, and compatibility before application components depend on them.
