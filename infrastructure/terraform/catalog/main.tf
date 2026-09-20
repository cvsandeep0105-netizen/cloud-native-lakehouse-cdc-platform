resource "aws_glue_catalog_database" "lakehouse" {
  name = "${local.name_prefix}_catalog"
}

resource "aws_athena_workgroup" "lakehouse" {
  name = "${local.name_prefix}-athena"

  configuration {
    enforce_workgroup_configuration    = true
    publish_cloudwatch_metrics_enabled = true

    result_configuration {
      encryption_configuration {
        encryption_option = "SSE_S3"
      }
    }
  }
}

output "glue_catalog_database" {
  value = aws_glue_catalog_database.lakehouse.name
}

output "athena_workgroup" {
  value = aws_athena_workgroup.lakehouse.name
}
