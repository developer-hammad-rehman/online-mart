import json
from typing import Annotated
from aiokafka import AIOKafkaProducer
from app.api.deps import FORMDEPS, DB_SESSION
from fastapi import APIRouter, Depends
from app.core.auth import get_user_by_username
from app.core.crud import add_user
from fastapi import HTTPException
from app.core.kafka import get_producer
from app.settings import KAFKA_NOTIFICATION_TOPIC

signup_router = APIRouter(tags=["Auth Routes"])


@signup_router.post("/register")
async def sign_up(
    form_data: FORMDEPS,
    session: DB_SESSION,
    producer: Annotated[AIOKafkaProducer, Depends(get_producer)],
):
    user = get_user_by_username(username=form_data.username, session=session)
    if user:
        raise HTTPException(status_code=401, detail="Email Already Exist")
    else:
        user = add_user(
            username=form_data.username, password=form_data.password, session=session
        )
        # await producer.send_and_wait(
        #     "user", json.dumps(user.model_dump()).encode("utf-8")
        # )
        await producer.send_and_wait(
            KAFKA_NOTIFICATION_TOPIC,
            json.dumps({"type": "register", "email": form_data.username}).encode(
                "utf-8"
            ),
        )
        return user
