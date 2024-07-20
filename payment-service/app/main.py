import re
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.kafka import event_up 
from app.db_config import create_table
import stripe
from app.depends import PRODUCER
from app.models import PaymentForm
from app.settings import STRIPE_KEY , KAFKA_TOPIC
from app import payment_pb2



stripe.api_key = STRIPE_KEY

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    event_up()
    yield




app = FastAPI(title="Payment Service",lifespan=lifespan)


@app.get('/')
def read_root():
    return {"message": "Payemmt Service"}



@app.post('/create-payment-intent')
async def create_payment_intent(request:PaymentForm, producer:PRODUCER):
    try:
        intent = stripe.PaymentIntent.create(
            amount=request.amount,
            currency='usd',
            payment_method=request.payment_id,
        )
        proto_buf = payment_pb2.Payment(amount = request.amount , curreny = "usd" , status=intent.status) # type: ignore
        serialized_string = proto_buf.SerializeToString()
        await producer.send(KAFKA_TOPIC , serialized_string)
        return {'clientSecret': intent.client_secret}
    except Exception as e:
        return {'error': str(e)}