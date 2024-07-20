from typing import Annotated
from fastapi import Depends
from app.db_config  import get_session , Session
from aiokafka import AIOKafkaProducer
from app.core.kafka import get_kafka_producer


DBSESSION = Annotated[Session , Depends(get_session)]

PRODUCER = Annotated[AIOKafkaProducer , Depends(get_kafka_producer)]