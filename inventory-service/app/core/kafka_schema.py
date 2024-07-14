from aiokafka import AIOKafkaProducer
from app.settings import KAFKA_PORT

async def get_kafka_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_PORT,
    )
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()