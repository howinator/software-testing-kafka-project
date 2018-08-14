import file_util as file_util
import kafka_util
import aws_util

def main():
    test_cases = file_util.get_test_cases()
    instance_id = ''  # TODO
    for test in test_cases:
        if test['metadata']['node_should_fail']:
            aws_util.kill_ec2_instance(instance_id)
        kafka_util.push_test_data_to_kafka(test['data'])

if __name__ == '__main__':
    main()