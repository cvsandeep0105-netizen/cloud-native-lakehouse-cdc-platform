resource "aws_cloudwatch_log_group" "data_platform" {
  name              = "/project02/${var.environment}/data-platform"
  retention_in_days = 30
}

resource "aws_cloudwatch_log_group" "glue" {
  name              = "/project02/${var.environment}/glue"
  retention_in_days = 30
}

resource "aws_cloudwatch_log_group" "athena" {
  name              = "/project02/${var.environment}/athena"
  retention_in_days = 30
}

output "data_platform_log_group" {
  value = aws_cloudwatch_log_group.data_platform.name
}

output "glue_log_group" {
  value = aws_cloudwatch_log_group.glue.name
}

output "athena_log_group" {
  value = aws_cloudwatch_log_group.athena.name
}
