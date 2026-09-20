# Area 02 Evidence

## CDC Validation Evidence

This directory contains binary CDC stream artifacts captured during the controlled local PostgreSQL logical-decoding validation performed in Area 02.

These files are retained as technical evidence. They are not application data and are not intended to represent a production CDC stream.

| Artifact | Size | Validation Purpose |
|---|---:|---|
| cdc_test_output.bin | 246 bytes | Controlled INSERT CDC capture |
| cdc_update_output.bin | 254 bytes | Controlled UPDATE CDC capture |
| cdc_delete_output.bin | 179 bytes | Controlled DELETE CDC capture |

## Validation Boundary

- PostgreSQL 18.4 was validated locally.
- Logical decoding was enabled with wal_level=logical.
- The built-in pgoutput output plugin was used.
- A logical replication slot and publication were created for the controlled test.
- INSERT, UPDATE, and DELETE operations were captured and their payload contents were verified.
- LSN progression was observed.
- The temporary publication and replication slot were removed after validation.
- Final verification confirmed that no temporary publication or replication slot remained.

## Claim Integrity

These artifacts establish local PostgreSQL CDC verification only.

They do not establish AWS DMS execution, AWS deployment, or production CDC operation.
