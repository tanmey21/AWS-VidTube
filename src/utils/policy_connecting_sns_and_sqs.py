from src.utils.configure_boto3 import client_connect
import json
def policy_connecting_sns_and_sqs(topic_arn: str, queue_arn: str) -> dict:
    policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "sns.amazonaws.com"},
                "Action": "SQS:SendMessage",
                "Resource": queue_arn,
                "Condition": {"ArnEquals": {"aws:SourceArn": topic_arn}}
            }]
        }
    return policy

def create_sqs_queue_with_sns_subscription(queue_name, topic_name):
    sqs = client_connect("sqs")
    queue = sqs.create_queue(QueueName=queue_name,
                             Attributes={
                                 'FifoQueue': 'true',
                                 'ContentBasedDeduplication': 'true'  # Optional: enables automatic deduplication
                             }
                             )
    queue_url = queue['QueueUrl']
    attrs = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['QueueArn'])
    queue_arn = attrs['Attributes']['QueueArn']

    return [queue_url, queue_arn]

def create_subscription(queue_arn, topic_arn , codec_need = False):
    sqs = client_connect("sqs")
    sns = client_connect("sns")
    policy = policy_connecting_sns_and_sqs(topic_arn , queue_arn)

    # Set the policy on the SQS queue
    sqs.set_queue_attributes(
        QueueUrl=sqs.get_queue_url(QueueName=queue_arn.split(':')[-1])['QueueUrl'],
        Attributes={
            'Policy': json.dumps(policy)
        }
    )
    filter_policy = {"codec": [{"exists": codec_need}]}
    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='sqs',
        Endpoint=queue_arn,
        # Attributes={
        #     'FilterPolicy': json.dumps(filter_policy)
        # }
    )

