from typing import Annotated
from aiokafka import AIOKafkaProducer
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from sqlmodel import Session
from app.db import get_session
from fastapi import Depends
from app.core.kafka import get_producer

OAUTH_SCHEMA  = OAuth2PasswordBearer(tokenUrl="auth")

DB_SESSION = Annotated[Session , Depends(get_session)]


FORMDEPS = Annotated[OAuth2PasswordRequestForm , Depends()]

OUATH2DEPS = Annotated[str , Depends(OAUTH_SCHEMA)]

PRODUCERDEPS = Annotated[AIOKafkaProducer , Depends(get_producer)]