import token
from sqlalchemy import true
import stripe
from app.models import PaymentForm
from app.settings import STRIPE_KEY
from fastapi import APIRouter , HTTPException


payment_router = APIRouter()

stripe.api_key = STRIPE_KEY

@payment_router.post("/create-payment-intent")
def create_payment_intent(payment: PaymentForm):
    try:
        intent = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency="USD",
        )
        return {"client_secret":intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))