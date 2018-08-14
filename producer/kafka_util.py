from kafka import KafkaProducer


def push_test_data_to_kafka(data):
    producer = KafkaProducer(bootstrap_servers='52.205.65.22:9092')
    producer.send('test_kafka', data.encode('utf-8'))
    producer.close()
