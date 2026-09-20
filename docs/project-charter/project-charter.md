# Project 02 — Cloud-Native Lakehouse, CDC & AI-Ready Data Platform on AWS

## 1. Project Identity

**Primary professional identity:** Data Engineer

**Specialization:** Data Engineering + Cloud Data Platforms + Streaming + AI-enabled Data Systems

**Project focus:** Cloud-native data platform engineering using real-world operational data, CDC, lakehouse architecture, incremental processing, governance, reliability, security, observability, and AI-assisted data engineering.

## 2. Business Problem

Modern organizations need analytical data platforms that can reliably transform continuously changing operational data into trusted, governed, queryable datasets without repeatedly rebuilding entire datasets.

This project addresses that problem by engineering a cloud-oriented lakehouse platform capable of ingesting an initial operational snapshot and subsequent changes, preserving raw history, applying CDC correctly, producing trusted Silver and Gold datasets, and exposing curated data for analytical consumption.

## 3. Engineering Problem

The core engineering problem is to reliably capture, preserve, process, validate, and serve changing operational data while maintaining correctness, idempotency, replayability, traceability, security, observability, performance, and cost awareness.

The platform must handle initial loads, incremental changes, inserts, updates, deletes where meaningful, duplicate delivery, ordering, late-arriving changes, retries, failures, backfills, schema evolution, and data-quality violations.

## 4. Primary Engineering Objectives

- Build a production-oriented cloud data platform.
- Use real-world relational business data.
- Implement a defensible CDC architecture.
- Separate immutable raw data from trusted and curated data.
- Implement Bronze, Silver, and Gold data layers.
- Use columnar storage and an appropriate lakehouse table format.
- Implement incremental processing.
- Provide safe retries, replay, backfill, and idempotent processing.
- Enforce deterministic data-quality gates.
- Implement metadata, catalog, and lineage capabilities.
- Provide orchestration and operational observability.
- Apply security and least-privilege principles.
- Implement automated testing and CI/CD.
- Measure performance and scalability using real execution evidence.
- Engineer for cloud cost awareness.
- Introduce an AI-assisted data-engineering capability without making AI the primary project identity.
- Produce evidence that can withstand Senior/Lead Data Engineer interview discussion.

## 5. Project 01 Differentiation

Project 01 demonstrates real-time streaming and AI-enabled EV telemetry processing.

Project 02 focuses primarily on cloud data platform engineering, CDC, lakehouse storage, incremental processing, governance, reliability, and analytical data delivery.

Project 02 therefore complements rather than duplicates Project 01.

## 6. Data Source Principle

The project will use real-world data wherever realistically possible.

The recommended source is the Olist Brazilian E-Commerce Public Dataset. Because the public dataset is historical and static, any generated change stream derived from it will be explicitly documented as CDC simulation/replay unless a genuine CDC source is actually deployed and verified.

No simulated CDC mechanism will be represented as genuine production-source CDC.

## 7. Cloud Principle

AWS is the target cloud platform.

AWS services will be selected based on engineering requirements rather than technology-list inflation.

Potential services include Amazon S3, AWS Glue, Glue Data Catalog, Amazon Athena, AWS DMS, Amazon RDS/Aurora, Step Functions, EventBridge, CloudWatch, IAM, KMS, Secrets Manager, and appropriate governance services where justified.

Actual AWS deployment will only be claimed when it is genuinely deployed and verified.

## 8. Local-First Engineering Principle

Development will primarily use Windows, VS Code, PowerShell, Git, GitHub CLI, Python, SQL, PostgreSQL, and appropriate local data-processing tooling.

Local validation will be used wherever practical to control cost and accelerate development.

Local validation will never be represented as proof of AWS production deployment.

## 9. Engineering Quality Principles

- Preserve working components.
- Investigate failures before modifying code.
- Verify root causes before making changes.
- Make the smallest appropriate change.
- Run targeted regression tests after every fix.
- Avoid unnecessary dependencies.
- Avoid speculative commands.
- Never fabricate metrics, deployments, costs, or production claims.
- Maintain reproducibility.
- Maintain traceable engineering evidence.

## 10. Scope Boundary

Project 02 covers discovery, requirements, real data, operational source modeling, CDC, cloud storage, lakehouse engineering, incremental processing, data quality, governance, orchestration, reliability, security, observability, testing, CI/CD, infrastructure as code, performance, cost engineering, deployment, evidence, documentation, GitHub integration, Engineering Report creation, portfolio integration, and final acceptance.

Project 03 will later focus primarily on modern data warehousing, analytics engineering, semantic/business modeling, and BI-ready consumption.

## 11. Final Professional Outcome

The completed project must demonstrate that the author can design, implement, test, operate, secure, measure, document, and defend a modern cloud data platform rather than merely demonstrate individual technologies.

## 12. Project Completion Rule

Project 02 is complete only after all approved engineering areas have passed their acceptance gates, quantitative evidence has been collected, documentation is complete, the GitHub repository is finalized, the Engineering Report is available online, the existing portfolio has been updated without breaking Project 01, and final acceptance has been completed.
