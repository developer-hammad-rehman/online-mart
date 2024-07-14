from fastapi import FastAPI
from app.db import create_table
from contextlib import asynccontextmanager
from app.api.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app = FastAPI(
    title="Product Service",
    lifespan=lifespan,
    servers=[
        {
            "url": "https://maggot-still-reliably.ngrok-free.app",
            "description": "Ngrok server for testing",
        }
    ],
)


@app.get("/")
def root_route():
    return {"message": "Product Service"}


app.include_router(router)
