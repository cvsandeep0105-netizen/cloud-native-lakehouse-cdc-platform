# Area 19 — Iceberg Catalog Strategy

## Local Catalog
The initial implementation uses a local catalog suitable for deterministic development and validation.

## Table Namespace
Project 02 tables are isolated under the Project 02 Iceberg namespace.

## AWS Target
AWS Glue Data Catalog is the intended cloud catalog candidate for the AWS implementation.

## Boundary
The AWS Glue Catalog target is an architecture decision, not evidence of AWS execution.

## Metadata
Iceberg metadata remains part of the table-format control plane and is not treated as business data.
