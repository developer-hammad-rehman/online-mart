from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_db_and_tables
from app.api.api import router
from app.core.kafka_schema import event_up

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    event_up()
    yield

app = FastAPI(title="Inventory Service" , lifespan=lifespan)


@app.get('/' , tags=["Root Route"])
def root_route():
    return {"message": "Inventory Service"}


app.include_router(router)