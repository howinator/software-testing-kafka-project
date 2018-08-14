from kafka import KafkaProducer


def push_test_data_to_kafka(data):
    producer = KafkaProducer(bootstrap_servers='18.214.118.21:9091', client_id='howie-producer')
    producer.send('test_kafka', data.encode('utf-8'))
    producer.close()
