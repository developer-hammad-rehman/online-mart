from aiokafka import AIOKafkaConsumer
import asyncio
import logging
from app.setting import KAFKA_BOOTSTRAP_SERVERS , KAFKA_GROUP_ID , KAFKA_TOPIC
import json
from app.core.notification import send_notification

logging.basicConfig(level=logging.INFO)

async def notification_consumer():
    consumer = AIOKafkaConsumer(
        "notification",
        bootstrap_servers="broker:19092",  # type: ignore
        group_id="notification_group",
        auto_offset_reset="earliest",
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
