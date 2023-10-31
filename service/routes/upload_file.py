"""Service to upload a file."""
from os import environ

from fastapi import APIRouter, UploadFile
import boto3

from service.utils.types import ServiceResponse
from service.utils.utils import check_s3_bucket_exists

router = APIRouter()

s3_client = boto3.client(
    "s3",
    aws_access_key_id=environ["aws_access_key_id"],
    aws_secret_access_key=environ["aws_secret_access_key"],
)


@router.post("/upload_file")
async def upload_file(
    *,
    storage_name: str,
    file_name: str,
    file: UploadFile,
) -> ServiceResponse:
    """
    Endpoint function to upload a file.
    Returns the url to the object.
    """
    if not check_s3_bucket_exists(s3_client=s3_client, bucket_name=storage_name):
        return {
            "statusCode": 422,
            "body": {"message": f"Bucket {storage_name} does not exist."},
        }

    s3_client.upload_fileobj(
        file.file,
        storage_name,
        file_name,
    )
    return {
        "statusCode": 200,
        "body": {"url": f"https://{storage_name}.s3.amazonaws.com/{file_name}"},
    }
