import os
from json import dumps
import time

from kafka import KafkaProducer
from datetime import datetime

class Producer:

    def post_message(self):
        producer = KafkaProducer(
            value_serializer=lambda m: dumps(m).encode('utf-8'), 
            bootstrap_servers=['kafka1:9092','kafka2:9093','kafka3:9094']
        )
        i = 0
        while True:
            print('post ...')
            producer.send("test", value={"hello": "producer_%s".format(i)})
            i = i + 1
            time.sleep(5)

        return True

