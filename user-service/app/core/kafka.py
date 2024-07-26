import logging
import ssl
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import Depends
from app.settings import KAFKA_BOOTSTRAP_SERVERS
from app.settings import KAFKA_CONNECTION_STRING


logging.basicConfig(level=logging.INFO)



context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

async def get_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN",
        sasl_plain_username="$ConnectionString",
        sasl_plain_password=KAFKA_CONNECTION_STRING,
        ssl_context=context,
    )
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()