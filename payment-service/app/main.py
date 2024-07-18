from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.api import router
from app.db_config import create_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    # create_table()
    yield




app = FastAPI(title="Payment Service",lifespan=lifespan)


@app.get('/')
def read_root():
    return {"message": "Payemmt Service"}


app.include_router(router, prefix="/api/v1")