import boto3

instance_id = <“instanceID”>
ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        instance_id
    ],
)

print(response)
