# Encryption & KMS Security Strategy

## Encryption at Rest
- S3 data requires encryption.
- Lakehouse data requires encryption.
- Database storage should use approved encryption mechanisms.
- Backup and retained data must follow the same protection requirements.

## Encryption in Transit
- TLS/encrypted transport is required for production network communication where supported.
- Database connections should use encrypted transport.
- Service-to-service communication must use secure endpoints.

## KMS
- Production encryption keys are managed through AWS KMS.
- Key administration is separated from normal workload permissions.
- Workloads receive only required encrypt/decrypt permissions.
- Key policies must avoid unrestricted access.
- Key rotation and lifecycle management are controlled.

## Boundary
No KMS keys or AWS encryption resources are created in Area 33.
