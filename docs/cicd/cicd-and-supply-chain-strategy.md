# CI/CD & Software Supply Chain Strategy

## Purpose

Define a production-oriented CI/CD and software supply chain strategy for Project 02.

## Objectives

- Automate source validation.
- Validate Python code and tests.
- Validate Terraform configuration.
- Protect the main branch.
- Produce reproducible builds.
- Track dependency versions.
- Detect accidental secrets.
- Maintain auditable build evidence.
- Prevent unvalidated infrastructure deployment.

## CI Pipeline Boundary

The CI pipeline is intended to validate:

1. Repository structure
2. Python syntax
3. Python tests
4. Dependency consistency
5. Configuration safety
6. Terraform formatting
7. Terraform initialization
8. Terraform validation
9. Secret scanning
10. Documentation/evidence integrity

## CD Boundary

Continuous deployment must be separated from continuous integration.

Production deployment requires:

1. Successful CI
2. Artifact/version identification
3. Terraform plan review
4. Human approval
5. Controlled deployment
6. Post-deployment validation
7. Evidence capture

## Branching

The primary branch is protected.

Changes should enter the primary branch through reviewed pull requests after required automated checks pass.

## Dependency Governance

Dependencies must be:

- Explicitly versioned.
- Reviewable.
- Reproducible where practical.
- Updated through controlled changes.
- Validated before release.

## Secret Protection

Secrets must never be committed to source control.

Protected CI/CD secret stores or environment-level secret mechanisms must be used for runtime credentials.

## Supply Chain Controls

The project should maintain:

- Dependency lock information.
- Terraform provider lock information.
- Reviewable source changes.
- Automated validation.
- Secret detection.
- Build/test evidence.
- Versioned deployment artifacts.

## Deployment Safety

CI must not automatically create production AWS infrastructure.

Terraform deployment remains an explicit controlled operation.

## Current Project Boundary

Area 36 defines and implements the CI/CD foundation.

Actual AWS deployment remains deferred to Area 39.

Status: ACTIVE
