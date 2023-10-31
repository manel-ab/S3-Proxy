"""Utils module that can be used in several services."""


def check_s3_bucket_exists(*, s3_client, bucket_name: str) -> bool:
    """Creates a s3 bucket if non existent"""
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except s3_client.exceptions.ClientError:
        return False
