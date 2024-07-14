import asyncio
import logging
import ssl
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import Depends
import json
# from app.core.kong import create_consumer_in_kong , create_jwt_credential_in_kong
from app.settings import KAFKA_BOOTSTRAP_SERVERS


logging.basicConfig(level=logging.INFO)

KAFKA_TOPIC = "user"
KAFKA_GROUP_ID = "user_group"

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

async def get_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        security_protocol="SASL_SSL",
        sasl_mechanism="PLAIN",
        sasl_plain_username="$ConnectionString",
        sasl_plain_password="Endpoint=sb://online-mart.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=x2dl9eJJFoWr7jXkOC9YK+2qN6UMBVZxd+AEhAD1I40=",
        ssl_context=context,
    )
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()




# async def produce_message(message:str, aio_producer:AIOKafkaProducer = Depends(get_producer)):
#     try:
#         await aio_producer.start()
#         result = await aio_producer.send_and_wait(KAFKA_TOPIC , message.encode("utf-8"))
#         return result
#     except Exception as e:
#         print(str(e))
#     finally:
#         await aio_producer.stop()
    


async def user_consumer():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, # type: ignore
        group_id=KAFKA_GROUP_ID,
        auto_offset_reset="earliest"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            to_decode = bytes(msg.value).decode('utf-8') # type: ignore
            logging.info(f"Consumed message: {to_decode}")
            user = json.loads(to_decode)
            print(user["username"])
            # create_consumer_in_kong(user["username"])
            # create_jwt_credential_in_kong(user_name=user["username"] , k_id=user["k_id"])
    except Exception as e:
        logging.error(f"Kafka Error: {str(e)}")
    finally:
        await consumer.stop()

async def start_consumer_with_retries():
    retries = 5
    for attempt in range(retries):
        try:
            await user_consumer()
            break
        except Exception as e:
            logging.error(f"Failed to start consumer, attempt {attempt + 1}/{retries}: {e}")
            await asyncio.sleep(5)

async def event_up():
    asyncio.create_task(start_consumer_with_retries())