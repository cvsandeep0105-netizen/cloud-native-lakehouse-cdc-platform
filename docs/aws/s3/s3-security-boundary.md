# Area 16 — S3 Security Boundary

## Required Controls
- S3 Block Public Access enabled.
- Bucket ownership controlled by the account.
- Server-side encryption enabled.
- IAM-based access control.
- Least privilege for application roles.
- No long-lived credentials embedded in code.
- Access logging and audit integration evaluated according to environment.

## Sensitive Data
Project 02 uses anonymized public Olist data. The platform nevertheless follows production-grade security principles.

## Secrets
Credentials and secrets must remain outside Git-tracked source files.

## AWS Claim Boundary
Security controls are design requirements until AWS execution is independently verified.
