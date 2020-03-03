import os
from json import dumps

from kafka import KafkaProducer
from datetime import datetime

class Producer:

    def post_message(self, m):
        producer = KafkaProducer(
            value_serializer=lambda m: dumps(m).encode('utf-8'), 
            bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094']
        )
        print('post ...')
        producer.send("test", value={"hello": "producer_%s".format(m)})

        return True

