from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_table
from app.core.kafka import event_up
from app.api.api import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    # await event_up()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router)