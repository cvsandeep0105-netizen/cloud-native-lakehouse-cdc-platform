variable "aws_region" {
  description = "AWS region for Project 02."
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project identifier."
  type        = string
  default     = "project02-lakehouse-cdc"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "stage", "prod"], var.environment)
    error_message = "Environment must be dev, stage, or prod."
  }
}
