# Secrets Management & Credential Security

## Controls
- Secrets never committed to Git.
- Credentials supplied at runtime.
- PostgreSQL credentials separated from administrative credentials.
- AWS workloads use IAM identities rather than embedded access keys.
- Production secrets use an approved secret-management mechanism.
- Logs and evidence must not expose secret values.
- Docker images must not contain credentials.
- Secret rotation must not require source-code changes.
- AI components cannot retrieve or modify secrets autonomously.

## Boundary
Real credentials are not created, retrieved, displayed, rotated, or modified by Area 33.
