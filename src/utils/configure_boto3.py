import boto3

def client_connect(service_name):
    client = boto3.client(service_name,
                          region_name='us-east-1',
                          aws_access_key_id='AKIAW4QRUXAW3BTBVTUM',
                          aws_secret_access_key='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',
                         )
    return client