from src.utils.policy_connecting_sns_and_sqs import create_sqs_queue_with_sns_subscription, create_subscription
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


if '__main__' == __name__:
    topic_arn = 'arn:aws:sns:us-east-1:473557153837:my_topic.fifo'  # Replace with your SNS topic ARN
    queue_name = 'my_writer_queue.fifo'  # SQS FIFO queue names must end with .fifo
    queue_url, queue_arn = create_sqs_queue_with_sns_subscription(queue_name, topic_arn)
    create_subscription(queue_arn, topic_arn , True)
    logger.info(f'SQS write queue {queue_url} created')
