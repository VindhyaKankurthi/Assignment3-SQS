
import boto3
from config import my_queue_name



sqs = boto3.resource('sqs')

#creating a queue
queue = sqs.create_queue(
    QueueName="myFirstQueue"
)
print(queue.url +  " queue created")

#sending a message
sqs = boto3.client('sqs')

def send_message(message):
   
    result = sqs.get_queue_url(QueueName=my_queue_name)
    queue_url = result['QueueUrl']

    result = sqs.send_message(
        QueueUrl=queue_url, 
        MessageBody=message)
    return result

result = send_message('This is the message in the queue')
print(result)
    
