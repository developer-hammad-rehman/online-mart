import asyncio
import logging
import ssl
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from app.core.kafka_controllers import add_payment_intent
from app.settings import KAFKA_BOOTSTRAP_SERVER ,   KAFKA_CONNECTION_STRING , KAFKA_TOPIC , KAFKA_GROUP_ID
from app import payment_pb2

logging.basicConfig(level=logging.INFO)

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

async def get_kafka_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN",
        sasl_plain_username="$ConnectionString",
        sasl_plain_password=KAFKA_CONNECTION_STRING,
        ssl_context=context,
    )
    await producer.start() # type: ignore
    try:
     yield producer
    finally:
       await producer.stop()



async def payment_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
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
            msg_decode = payment_pb2.Payment() # type: ignore
            msg_decode.ParseFromString(msg.value)
            add_payment_intent(msg_decode)
            logging.info(f"Message Consumed {msg_decode}")
    except Exception as e:
        logging.error(f"Kafka Error: {str(e)}")
    finally:
        await consumer.stop()

def event_up():
    asyncio.create_task(payment_consumer())