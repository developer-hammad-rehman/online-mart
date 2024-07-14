import ssl
from aiokafka import AIOKafkaConsumer
import asyncio
import logging
from app.setting import KAFKA_BOOTSTRAP_SERVERS , KAFKA_GROUP_ID , KAFKA_TOPIC , KAFKA_CONNECTION_STRING
import json
from app.core.notification import send_notification

logging.basicConfig(level=logging.INFO)


context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

async def notification_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
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
            send_notification(decode_json)
    except Exception as e:
        logging.error(f"Kafka Error: {str(e)}")
    finally:
        await consumer.stop()


async def start_consumer_with_retries():
    retries = 5
    for attempt in range(retries):
        try:
            await notification_consumer()  # type: ignore
            break
        except Exception as e:
            logging.error(
                f"Failed to start consumer, attempt {attempt + 1}/{retries}: {e}"
            )
            await asyncio.sleep(5)


async def event_up():
    asyncio.create_task(start_consumer_with_retries())
