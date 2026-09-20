locals {
  name_prefix = "${var.project_name}-${var.environment}"
}

module "s3" {
  source      = "./s3"
  name_prefix = local.name_prefix
  kms_key_arn = module.kms.data_lake_kms_key_arn
}

module "kms" {
  source      = "./kms"
  name_prefix = local.name_prefix
}

module "catalog" {
  source      = "./catalog"
  name_prefix = local.name_prefix
}

module "iam" {
  source      = "./iam"
  name_prefix = local.name_prefix
}

module "monitoring" {
  source      = "./monitoring"
  environment = var.environment
}
