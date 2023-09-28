import boto3
import pathlib
import io

aws_region = "eu-north-1"
s3_bucket_name = "alex13"

#Скачаємо файл, або папку з S3 bucket
s3_client = boto3.client("s3", region_name=aws_region)
s3_client.download_file(s3_bucket_name,"example_name_currency.txt", r"d:\Download\example_s3bucket_currency.txt'")
print('S3 object download complete')
