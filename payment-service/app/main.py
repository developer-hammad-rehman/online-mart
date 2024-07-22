from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.kafka import event_up 
from app.db_config import create_table
from app.routes import payment_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    # event_up()
    yield




app = FastAPI(title="Payment Service", lifespan=lifespan)


@app.get('/')
def read_root_route():
    return {"message": "Payemmt Service"}


app.include_router(payment_routes.router)