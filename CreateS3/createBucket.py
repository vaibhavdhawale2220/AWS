import boto3

s3_client = boto3.client('s3')
resp = s3_client.create_bucket(
    ACL='private',
    Bucket='todayclass2june2022',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)
