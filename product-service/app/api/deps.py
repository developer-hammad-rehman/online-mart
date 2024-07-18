from app.core.kafka_schema import get_producer
from app.db import get_session
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from aiokafka import AIOKafkaProducer

PRODUCERDEPS = Annotated[AIOKafkaProducer , Depends(get_producer)]

DBSESSION = Annotated[Session , Depends(get_session)]