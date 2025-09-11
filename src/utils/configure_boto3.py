import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def client_connect(service_name):
    client = boto3.client(service_name,
                          region_name=os.getenv('REGION_NAME'),
                          aws_access_key_id=os.getenv('ACCESS_KEY'),
                          aws_secret_access_key=os.getenv('SECRET_KEY'),
                         )
    return client