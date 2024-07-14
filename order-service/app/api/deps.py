from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from app.db import get_session
from aiokafka import AIOKafkaProducer
from app.core.kafka_schema import get_producer

DBSESSION = Annotated[Session , Depends(get_session)]

PRODUCERDEP = Annotated[AIOKafkaProducer , Depends(get_producer)]