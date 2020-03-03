import time

from api_producer.objects import Producer
from api_producer.config import *

RETURN_EXITOSO = True


def main():

    producer = Producer()
    for i in range(10):
        producer.post_message(i)
        time.sleep(2)
    
    return RETURN_EXITOSO


if __name__ == "__main__":
    main()