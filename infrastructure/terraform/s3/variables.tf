variable "name_prefix" {
  description = "Resource name prefix."
  type        = string
}

variable "kms_key_arn" {
  description = "ARN of the customer-managed KMS key used for S3 encryption."
  type        = string
}
