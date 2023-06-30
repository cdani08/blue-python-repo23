import boto3
import json
from datetime import datetime

# Create SQS client
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    # Generate a random message content using the current time
    message_content = str(datetime.now())
    
    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl='YOUR_QUEUE_URL',
        MessageBody=message_content
    )
    
    # Print the response
    print("Message sent to SQS queue:", response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS queue')
    }