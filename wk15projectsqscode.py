import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='order-queue'
)

# Print the queue URL
print(response['QueueUrl'])


