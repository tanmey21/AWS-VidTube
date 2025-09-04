import boto3

def client_connect(service_name):
    client = boto3.client(service_name,
                          region_name='us-east-1',
                          aws_access_key_id='test',
                          aws_secret_access_key='test',
                          endpoint_url='http://localhost:4566')
    return client