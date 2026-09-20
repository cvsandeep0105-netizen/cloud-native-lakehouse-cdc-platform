# ADR-001 — Operational Source Platform

- Status: Accepted
- Decision ID: ADR-001
- Scope: Operational source database for Project 02

## 1. Context

Project 02 requires a relational operational source system representing realistic e-commerce entities and relationships. The source platform must support relational constraints, SQL-based validation, reproducible development, and a credible path toward cloud-based CDC.

The selected source platform will initially support local development and testing. An AWS-hosted equivalent may be evaluated later.

## 2. Requirements

- Relational data model.
- Primary and foreign-key constraints.
- Transactional consistency.
- SQL query capability.
- Indexing support.
- Reproducible local development.
- Compatibility with CDC patterns.
- Credible AWS deployment path.
- Reasonable development and operating cost.
- Strong documentation and ecosystem support.

## 3. Options

### Option A — PostgreSQL

Open-source relational database suitable for local development and production workloads. AWS provides managed PostgreSQL-compatible deployment options.

### Option B — Aurora PostgreSQL

AWS-managed PostgreSQL-compatible database service designed for cloud workloads with managed operational capabilities.

### Option C — MySQL

Open-source relational database with broad ecosystem support and AWS managed deployment options.

## 4. Evaluation Criteria

| Criterion | PostgreSQL | Aurora PostgreSQL | MySQL |
|---|---|---|---|
| Local development | Strong | Limited as a local equivalent | Strong |
| Relational modeling | Strong | Strong | Strong |
| SQL capability | Strong | Strong | Strong |
| CDC compatibility | Strong candidate | Strong candidate | Strong candidate |
| AWS integration | Strong | Native AWS option | Strong |
| Local reproducibility | Strong | Lower | Strong |
| Operational management | Requires local administration | AWS managed | Requires local administration |
| Development cost | Low | AWS-dependent | Low |
| Portfolio relevance | Strong | Strong AWS relevance | Strong |

## 5. Current Assessment

PostgreSQL is the selected local-development platform because it provides strong relational capabilities, low local operating cost, reproducibility, and a credible migration path to AWS-managed PostgreSQL-compatible infrastructure.

Aurora PostgreSQL is a strong AWS production candidate but should not be used merely to make the local project appear cloud-native.

MySQL remains a viable alternative but provides no demonstrated requirement advantage over PostgreSQL at this stage.

## 6. Decision Status

PostgreSQL is accepted as the operational source platform for the local Project 02 implementation.

The decision is supported by successful local validation of the required relational capabilities and PostgreSQL logical CDC capability. PostgreSQL 18.4 was verified locally, logical decoding was enabled with wal_level=logical, and a controlled pgoutput CDC test successfully captured INSERT, UPDATE, and DELETE changes.

Aurora PostgreSQL remains a credible AWS-managed deployment candidate, but AWS deployment has not been executed or runtime-validated. MySQL remains a viable alternative but is not selected because no demonstrated project requirement provides an advantage over PostgreSQL.

### Validation Evidence

- PostgreSQL 18.4 locally verified.
- Logical decoding configuration successfully activated.
- Replication authentication prerequisites verified.
- pg_recvlogical 18.4 availability verified.
- Logical replication slot created with pgoutput.
- Publication created and verified for INSERT, UPDATE, DELETE, and TRUNCATE.
- Controlled INSERT, UPDATE, and DELETE operations captured through PostgreSQL logical decoding.
- CDC payload contents and source values verified.
- LSN progression and confirmed_flush_lsn observed.
- Temporary publication and replication slot removed after validation.
- Final verification confirmed no temporary publication or replication slot remained.

### Claim Boundary

This acceptance establishes PostgreSQL as the locally verified operational source platform and locally verified CDC-capable database.

It does not claim that Aurora PostgreSQL or AWS DMS has been deployed or executed.
