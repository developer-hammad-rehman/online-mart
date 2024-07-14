from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.kafka_schema import event_up
from app.models import CustomNotification
from app.core.notification import send_custom_notification

@asynccontextmanager
async def lifespan(app: FastAPI):
    await event_up()
    yield

app = FastAPI(title="Notification Service", lifespan=lifespan)

@app.get("/", tags=["Root Route"])
def root_route():
    return {"message": "Notification Service is running"}


@app.post('/custom-notification')
def custom_notification(request:CustomNotification):
    send_custom_notification(username=request.username , message=request.message)
    return {"message": "Notification is send"}