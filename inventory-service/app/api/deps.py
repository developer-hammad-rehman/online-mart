from aiokafka import AIOKafkaProducer
from fastapi import Depends
from typing import Annotated

from sqlmodel import Session

from app.core.kafka_schema import get_producer
from app.db import get_session

PRODUCERDEPS = Annotated[AIOKafkaProducer , Depends(get_producer)]

DBSESSIONDEPS = Annotated[Session, Depends(get_session)]