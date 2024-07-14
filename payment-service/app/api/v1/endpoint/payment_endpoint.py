import token
import stripe
from app.models import PaymentForm
from app.settings import STRIPE_KEY
from fastapi import APIRouter , HTTPException


payment_router = APIRouter()

stripe.api_key = STRIPE_KEY

@payment_router.post("/create-payment-intent")
def create_payment_intent(payment: PaymentForm):
    try:
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": payment.card_number,
                "exp_month": payment.exp_month,
                "exp_year": payment.exp_year,
                "cvc": payment.cvc,
            },
        )
        intent = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency="usd",
            payment_method=payment_method.id,
            confirm=True,
            confirmation_method="manual"
        )
        return {"intent":intent}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))