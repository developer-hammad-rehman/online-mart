import asyncio
import logging
from app.core.kafka_order import kafka_order_status
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json
import ssl
from app.settings import KAFKA_GROUP_ID, KAFKA_PORT, KAFKA_TOPIC , KAFKA_CONNECTION_STRING

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
            decode_json = json.loads(bytes(msg.value).decode("utf-8"))  # type: ignore
            logging.info(f"Consumed message: {decode_json}")
            kafka_order_status(decode_json)
    except Exception as e:
        logging.error(f"Kafka Error: {str(e)}")
    finally:
        await consumer.stop() # type: ignore


async def start_consumer_with_retries():
    retries = 5
    for attempt in range(retries):
        try:
            await order_consumer()  # type: ignore
            break
        except Exception as e:
            logging.error(
                f"Failed to start consumer, attempt {attempt + 1}/{retries}: {e}"
            )
            await asyncio.sleep(5)


async def event_up():
    asyncio.create_task(start_consumer_with_retries())
