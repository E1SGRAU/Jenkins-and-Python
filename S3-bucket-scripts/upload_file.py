import boto3
import pathlib
import io

aws_region = "eu-north-1"
s3_bucket_name = "alex13"

#Загрузка файлів на S3 bucket
s3_client = boto3.client("s3", region_name=aws_region)

#Шлях до файлу, або папки що треба загрузити на S3 bucket
local_file_path = r"d:\Download\currency.txt'"

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = pathlib.Path(file_name).name  
    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{object_name}' has been uploaded to '{bucket}'")

upload_files(local_file_path, s3_bucket_name, "example_name_currency.txt")
