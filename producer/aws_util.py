# import boto3

# def kill_ec2_instance(instance_id):
#     ec2 = boto3.resource('ec2')
#     ec2.instances.filter(InstanceIds=[instance_id]).stop()