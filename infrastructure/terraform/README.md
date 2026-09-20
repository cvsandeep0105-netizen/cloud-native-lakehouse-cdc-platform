# Project 02 Terraform Infrastructure

Terraform definitions for the AWS infrastructure of Project 02.

## Environments

- dev
- stage
- prod

## Security

- No credentials are stored in Terraform source.
- Environment-specific values are supplied through variables.
- Infrastructure follows least privilege.
- Terraform state is treated as sensitive.

## Deployment

Area 35-B defines the Terraform workspace/provider foundation.

AWS resources are NOT created by this subarea.
