import boto3
import pathlib
import io

aws_region = "eu-north-1"
s3_bucket_name = "alex13"

#Створимо S3 bucket 
s3_client = boto3.resource("s3", region_name=aws_region)
location = {'LocationConstraint': aws_region}
bucket = s3_client.create_bucket(
    Bucket=s3_bucket_name,
    CreateBucketConfiguration=location)
print("Amazon S3 bucket has been created")

#Перевірка створеного S3 bucket-ту
iterator = s3_client.buckets.all()
print("show list of buckets")
for bucket in iterator:
    print(f"--{bucket.name}")
