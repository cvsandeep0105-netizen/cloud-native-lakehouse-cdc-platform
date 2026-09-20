# Network & Data Access Security

## Network Boundary
- Internal data services must not be publicly exposed by default.
- Production databases require restricted network access.
- Workloads communicate through approved network paths.
- Administrative access is separately controlled.

## Data Access
- Raw data write access is restricted to ingestion identities.
- Bronze/Silver processing access is workload-specific.
- Gold analytical access is read-oriented where possible.
- Quarantine data has controlled access.
- Metadata access is separated from unrestricted data mutation.

## Environment Separation
- Development, test, and production access must be separated.
- Cross-environment access requires explicit authorization.

## Boundary
Area 33 defines the architecture only. No VPC, security group, endpoint, bucket policy, or AWS network resource is deployed.
