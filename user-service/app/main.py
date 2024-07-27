from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_table
from app.api.api import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield

app = FastAPI(
title="User Service",
lifespan=lifespan,
servers=[
    {
        "url": "https://user-service.bluedune-2d8c02d1.eastus.azurecontainerapps.io",
        "description": "Production Url",
    }
]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router)