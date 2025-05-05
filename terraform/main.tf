provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "fastapi_demo_bucket" {
  bucket = "fastapi-demo-bucket-${random_id.bucket_id.hex}"
  acl    = "private"

  tags = {
    Name        = "FastAPI Demo Bucket"
    Environment = "Dev"
  }
}

resource "random_id" "bucket_id" {
  byte_length = 4
}
