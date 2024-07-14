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
            "url": "https://product-service.bluedune-2d8c02d1.eastus.azurecontainerapps.io",
            "description": "Production Url",
        }
    ],
)


@app.get("/")
def root_route():
    return {"message": "Product Service"}


app.include_router(router)
