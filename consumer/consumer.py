from confluent_kafka import Consumer, KafkaError


c = Consumer({
    'bootstrap.servers': 'ec2-52-200-128-8.compute-1.amazonaws.com:9093',
    'group.id': '1',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
})

c.subscribe(['test_kafka'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()