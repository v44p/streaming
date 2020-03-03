from api_producer.objects import Producer
from api_producer.config import *

RETURN_EXITOSO = True

def main():

    producer = Producer()
    producer.post_message()
    return RETURN_EXITOSO


if __name__ == "__main__":
    main()