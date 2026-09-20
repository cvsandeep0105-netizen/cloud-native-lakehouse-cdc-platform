# Project 02 — Engineering Standards

## Purpose
This document defines the mandatory engineering standards for Project 02.

## Engineering Principles
- Production-oriented engineering over demo-oriented implementation.
- Small, testable, deterministic changes.
- Preserve previously validated behavior.
- Prefer explicit configuration over hidden defaults.
- Separate source, transformation, orchestration, infrastructure, tests, and documentation boundaries.

## Python Standards
- Python 3.11 is the project runtime.
- Use clear module and function boundaries.
- Prefer type hints for production-facing interfaces.
- Avoid hard-coded credentials, endpoints, and environment-specific secrets.
- Keep functions focused and testable.

## Data Engineering Standards
- Preserve source-system truth and document transformations.
- Treat raw data as immutable.
- Make incremental processing deterministic and restart-safe.
- Record record counts and processing outcomes where operationally relevant.
- Data quality failures must be observable and traceable.

## CDC Standards
- Distinguish genuine CDC from simulated or replayed change streams.
- Preserve operation type, ordering metadata, source identity, and event timestamps where available.
- Design downstream processing for duplicates and safe reruns.
- Never claim AWS CDC execution without AWS execution evidence.

## Configuration Standards
- Environment-specific configuration must not be hard-coded into application logic.
- Secrets must never be committed to Git.
- Use .env.example or documented configuration contracts when environment variables are required.
- Keep configuration names explicit and consistent.

## Testing Standards
- Every production-facing component should have deterministic tests.
- Tests must verify both expected behavior and important failure paths.
- Regression tests are required when a defect is fixed.
- Environment smoke tests are separate from application tests.

## Logging & Observability Standards
- Prefer structured, machine-readable operational logging.
- Include useful execution context such as component, operation, status, duration, and record counts where applicable.
- Never log passwords, access keys, tokens, or other secrets.

## Security Standards
- Apply least-privilege access.
- Separate application, data, and infrastructure responsibilities where practical.
- Protect secrets through approved secret-management mechanisms.
- Treat local credentials and AWS credentials as sensitive.

## Git Standards
- Keep commits focused and traceable.
- Do not commit secrets, virtual environments, generated data, temporary files, or runtime artifacts.
- Use descriptive commit messages.
- Validate changes before committing.

## Documentation Standards
- Architecture decisions must be documented through ADRs where appropriate.
- Operational assumptions and limitations must be explicit.
- Evidence must distinguish designed, locally verified, AWS-configured, AWS-executed, and production-observed states.

## Claim Integrity
- Never present a design as an execution result.
- Never fabricate AWS deployment, cost, performance, availability, or monitoring evidence.
- Clearly identify simulated CDC and locally verified CDC.
- Quantitative claims must have traceable evidence.

## Change Management
- Inspect before modifying.
- Isolate the failing component.
- Verify root cause before changing code.
- Make the smallest justified change.
- Run targeted regression validation.
- Preserve previously passing components.
