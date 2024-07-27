import asyncio
import logging
from app.core.kafka_order import kafka_order_status
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import ssl
from app.settings import KAFKA_GROUP_ID, KAFKA_PORT, KAFKA_TOPIC , KAFKA_CONNECTION_STRING
from app import order_pb2

logging.basicConfig(level=logging.INFO)

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

async def get_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_PORT,  # type: ignore
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



async def order_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_PORT,  # type: ignore
        group_id=KAFKA_GROUP_ID,
        auto_offset_reset="earliest",
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN", 
        sasl_plain_username="$ConnectionString",
        sasl_plain_password=KAFKA_CONNECTION_STRING,
        ssl_context=context,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            msg_decode  = order_pb2.Order() # type: ignore
            msg_decode.ParseFromString(msg.value)
            logging.info(f"Consumed message: {msg_decode}")
            kafka_order_status(msg_decode)
    except Exception as e:
        logging.error(f"Kafka Error: {str(e)}")
    finally:
        await consumer.stop() # type: ignore


async def event_up():
    asyncio.create_task(order_consumer())
