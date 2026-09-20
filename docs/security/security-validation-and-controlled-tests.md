# Security Validation & Controlled Tests

## Controlled Validation
- Secret files must remain excluded from Git.
- Evidence must contain no real credential values.
- Application identities must not receive unrestricted permissions.
- Query access must not imply write access.
- Production security controls must fail closed.
- AI components cannot bypass deterministic security controls.
- AWS deployment claims require actual AWS evidence.

## Test Boundary
Validation is design-level and local-safe. Tests do not create or alter production AWS resources.
