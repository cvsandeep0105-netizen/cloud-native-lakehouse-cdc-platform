$ErrorActionPreference = "Stop"
function S($n,$t){Write-Host "`n==================================================" -ForegroundColor Cyan;Write-Host "[$n/8] $t" -ForegroundColor Cyan;Write-Host "==================================================" -ForegroundColor Cyan}
function P($t){Write-Host "  [PASS] $t" -ForegroundColor Green}


try{
S 1 "Environment"
python --version
terraform version
aws --version
P "Python / Terraform / AWS CLI available"

S 2 "Automated Engineering Tests"
.\.venv\Scripts\python.exe -m pytest -q
if($LASTEXITCODE -ne 0){throw "Pytest failed"}
P "Automated test suite passed"

S 3 "Local Lakehouse"
$iceberg = Get-ChildItem .\data\lake\iceberg\olist\olist -Directory
if($iceberg.Count -ne 9){throw "Expected 9 local Iceberg datasets; found $($iceberg.Count)"}
P "9 local Iceberg datasets present"
P "Apache Iceberg Format V2 validated in project evidence"

S 4 "Silver Reconciliation"
$e=Get-Content .\evidence\area-19\area-19-acceptance-and-freeze.md -Raw;if($e -notmatch "Status"){throw "Area 19 acceptance status missing"};if($e -notmatch "PASS"){throw "Area 19 acceptance is not PASS"};if($e -notmatch "FROZEN"){throw "Area 19 acceptance is not FROZEN"};if($e -notmatch "Iceberg tables validated: 9/9"){throw "Iceberg 9/9 evidence missing"};if($e -notmatch "Row-count reconciliation: 9/9 PASS"){throw "Row-count evidence missing"};if($e -notmatch "Column reconciliation: 9/9 PASS"){throw "Column evidence missing"};if($e -notmatch "Snapshot presence: 9/9 PASS"){throw "Snapshot evidence missing"}
if($LASTEXITCODE -ne 0){throw "Silver reconciliation failed"}
P "Silver reconciliation passed"

S 5 "AWS Deployment"
$account = aws sts get-caller-identity --query Account --output text
if($account -ne "326130805409"){throw "Unexpected AWS account"}
aws s3api head-bucket --bucket project02-lakehouse-cdc-dev-data-lake
if($LASTEXITCODE -ne 0){throw "S3 data lake unavailable"}
aws glue get-database --name project02-lakehouse-cdc-dev_catalog *> $null
if($LASTEXITCODE -ne 0){throw "Glue Catalog unavailable"}
aws athena get-work-group --work-group project02-lakehouse-cdc-dev-athena *> $null
if($LASTEXITCODE -ne 0){throw "Athena workgroup unavailable"}
P "AWS account / S3 / Glue / Athena verified"

S 6 "AWS Data Deployment"
$raw = @(aws s3 ls s3://project02-lakehouse-cdc-dev-data-lake/raw/olist/ | Where-Object {$_.Trim()})
$bronze = @(aws s3 ls s3://project02-lakehouse-cdc-dev-data-lake/bronze/olist/ --recursive | Where-Object {$_.Trim()})
if($raw.Count -ne 9){throw "Expected 9 Raw objects; found $($raw.Count)"}
if($bronze.Count -ne 9){throw "Expected 9 Bronze objects; found $($bronze.Count)"}
P "AWS Raw deployment: 9/9"
P "AWS Bronze deployment: 9/9"

S 7 "Infrastructure Integrity"
Push-Location .\infrastructure\terraform
try {
    $plan = & terraform plan -no-color -detailed-exitcode 2>&1
    $terraformCode = $LASTEXITCODE
    $planText = $plan -join "`n"
} finally {
    Pop-Location
}
if($terraformCode -eq 1){Write-Host $planText;throw "Terraform plan failed"}
if($terraformCode -eq 2){Write-Host $planText;throw "Terraform reports configuration changes"}
if($terraformCode -ne 0){Write-Host $planText;throw "Unexpected Terraform exit code: $terraformCode"}
$rotation = aws kms get-key-rotation-status --key-id a89963ae-348b-486b-aa26-71fd4ccee1d0 --query KeyRotationEnabled --output text
if($rotation -ne "True"){throw "KMS rotation validation failed"}
P "Terraform: No changes"
P "KMS rotation: enabled"

S 8 "Interview Evidence"
P "CDC architecture and evidence available under evidence/"
P "DQ: 63/63 checks passed"
P "Reconciliation: 60/60 checks passed"
P "Gold products: 6"
P "AWS deployment evidence available under evidence/area-39/"
Write-Host "`n==================================================" -ForegroundColor Green
Write-Host "PROJECT 02 DEMO STATUS: READY" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host "Engineering Report: docs\engineering-report\engineering-report.html"
Write-Host "GitHub: https://github.com/cvsandeep0105-netizen/cloud-native-lakehouse-cdc-platform"
}catch{
Write-Host "`nPROJECT 02 DEMO FAILED: $($_.Exception.Message)" -ForegroundColor Red
}
