from fastapi import FastAPI
from app.db import create_table
from contextlib import asynccontextmanager
from app.api.api import router
from app.core.kafka_schema import event_up

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create_table()
    await event_up()
    yield

app = FastAPI(title="Order Service" , lifespan=lifespan )


@app.get("/" , tags=["Root Route"])
async def root_route():
    return {"message": "Order Service"}

app.include_router(router)