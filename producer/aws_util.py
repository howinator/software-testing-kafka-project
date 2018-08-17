import boto3
import json

def kill_ec2_instance(instance_id):
    aws_creds = get_aws_creds()
    client = boto3.client(
        "ec2",
        aws_access_key_id=aws_creds['access_key_id'],
        aws_secret_access_key=aws_creds['secret_key'],
        region_name='us-east-1'
    )
    # ec2 = boto3.resource('ec2')
    # client.instances.filter(InstanceIds=[instance_id]).stop()
    client.stop_instances(InstanceIds=[instance_id], DryRun=False)
    print("Broker instance stopped")


def start_ec2_instance(instance_id):
    aws_creds = get_aws_creds()
    client=boto3.client(
        "ec2",
        aws_access_key_id=aws_creds['access_key_id'],
        aws_secret_access_key=aws_creds['secret_key'],
        region_name='us-east-1'
    )
    print("Starting instance")
    client.start_instances(InstanceIds=[instance_id], DryRun=False)




def get_aws_creds():
    with open('aws-creds.json') as f:
        return json.load(f)