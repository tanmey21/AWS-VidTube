from utils.configure_boto3 import client_connect
from utils.constants import reader_queue_url
import time
sqs = client_connect("sqs")

while True:
    response = sqs.receive_message(
        QueueUrl=reader_queue_url,
        MaxNumberOfMessages=10,      # up to 10 at a time
        WaitTimeSeconds=2,           # long polling
        MessageAttributeNames=["All"],
        AttributeNames=["All"]
    )

    messages = response.get("Messages", [])
    if not messages:
        print("No current messages")

    for msg in messages:
        print(f"MessageId: {msg['MessageId']}, Body: {msg['Body']}, GroupId: {msg['Attributes'].get('MessageGroupId')}")

    time.sleep(3)
