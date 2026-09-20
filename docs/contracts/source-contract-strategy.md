# Project 02 — Source Data Contract Strategy

## Purpose
This document defines the source data contract strategy for Project 02.
The contract establishes the expected structural, relational, quality, and change boundaries for source data before downstream processing.

## Contract Scope
The source contract covers the nine Olist source datasets represented in the Project 02 operational PostgreSQL platform.
It defines expectations for schema, data types, nullability, keys, relationships, source-level quality observations, and change-event boundaries.

## Source of Truth
The published Olist dataset is the historical source of truth for the acquired source files.
PostgreSQL project02 is the operational relational representation of that source.
Downstream S3, Bronze, Iceberg, Silver, and Gold layers must not redefine source truth.

## Structural Contract
Each source dataset must have a documented dataset identity, expected columns, expected logical data types, and documented nullability.
Unexpected columns, missing columns, or incompatible type changes are contract violations unless explicitly approved through change control.

## Key Contract
Primary and candidate keys must be explicitly documented.
Source identifiers must be preserved.
Where the source does not provide a reliable unique identifier, a technical key may be introduced without modifying the source values.

## Relationship Contract
Documented parent-child relationships must be validated before dependent processing.
Referential-integrity failures must be surfaced as data-quality failures rather than silently corrected.

## Data Quality Contract
Source anomalies discovered during profiling are observations unless a later contract explicitly defines them as invalid.
Project 02 must preserve source truth and avoid silently changing source values to satisfy downstream expectations.
Deterministic data-quality rules remain authoritative for pipeline acceptance.

## CDC Boundary
The published Olist dataset is static historical data and is not itself a live CDC feed.
Any changes generated from the historical dataset are CDC simulation or replay.
Genuine local PostgreSQL logical CDC was verified in Area 02.
AWS DMS CDC execution must not be claimed without AWS runtime evidence.

## Enforcement Boundary
Structural and relational contract violations should block or quarantine affected processing where appropriate.
Documented source anomalies may be preserved and reported when they are valid characteristics of the source.
Contract enforcement must be deterministic and auditable.

## Versioning and Change Control
Source contracts are version-controlled documentation.
Any intentional contract change requires documented rationale, impact assessment, validation, and approval before dependent processing is changed.
Completed Areas remain frozen unless new evidence requires a controlled change.

## Claim Integrity
Contract documentation must distinguish source facts, observed profiling results, designed controls, locally verified behavior, and future AWS execution.
No AWS runtime capability may be represented as executed without corresponding evidence.
