import boto3
import json

def kill_ec2_instance(instance_id):
    aws_creds = get_aws_creds()
    client = boto3.client(
        "ec2",
        aws_access_key_id=aws_creds['access_key_id'],
        aws_secret_access_key=aws_creds['secret_key']
    )
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=[instance_id]).stop()


def get_aws_creds():
    with open('aws-creds.json') as f:
        return json.load(f)