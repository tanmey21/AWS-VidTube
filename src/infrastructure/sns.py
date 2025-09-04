import logging
from  src.utils.configure_boto3 import client_connect

logging.basicConfig(level=logging.INFO)

def create_sns_topic(topic_name):
    sns_client = client_connect('sns')
    response = sns_client.create_topic(Name=topic_name,Attributes={
        "FifoTopic": "true"
    })
    return response['TopicArn']

def publish_to_sns_topic(topic_arn, message):
    sns_client = client_connect('sns')
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    return response


if '__main__' == __name__:
    topic_arn = create_sns_topic('my_topic.fifo')
    logging.info(f'Created SNS topic: {topic_arn}')