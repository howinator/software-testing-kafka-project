from confluent_kafka import Consumer, KafkaError


c = Consumer({
    'bootstrap.servers': 'ec2-52-200-128-8.compute-1.amazonaws.com:9093',
    'group.id': '10',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
})

c.subscribe(['test_kafka'])

while True:
    msg = c.poll(1.0)
    msgValue = msg.value()
    if msgValue.decode('utf-8') != 'Broker: No more messages':
        f = open("testcase.txt", "r")
        fline = f.readline()
        for x in fline:
            if msgValue == 'Broker: No more messages':
                print('No messages at this point')
                break
            print('Received: ' + msgValue + "; Expected: " + x)
            msg = c.poll(1.0)
            msgValue = msg.value().decode('utf-8')

        # print('Received message: {}'.format(msg.value().decode('utf-8')))
        continue
    else:
        print('No messages at this point')
        break
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
c.close()
