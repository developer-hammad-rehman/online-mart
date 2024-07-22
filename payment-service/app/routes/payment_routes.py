from typing import Annotated, Optional
from fastapi import APIRouter
import stripe
from app.depends import DBSESSION, PRODUCER
from app.models import Payment, PaymentForm
from fastapi.responses import RedirectResponse
from app.settings import  STRIPE_KEY


stripe.api_key = STRIPE_KEY


router = APIRouter()

#=============================================================================================

@router.get("/checkout-payment")
async def checkout_payment(price: int, quantity: int):
    return RedirectResponse(
        f"https://martnest.vercel.app/payment?price={price}&quantity={quantity}"
    )

#=============================================================================================

@router.post("/create-payment-intent")
async def create_payment_intent(request: PaymentForm):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(request.amount),
            currency="usd",
        )
        return {"clientSecret": intent.client_secret}
    except Exception as e:
        return {"error": str(e)}

#===================================================================================================================

@router.get('/payment-intents')
async def list_payment_intents(customer_id: Annotated[Optional[str] , str] = None):
    try:
        intents = stripe.PaymentIntent.list(customer=customer_id) if customer_id else stripe.PaymentIntent.list()
        return intents
    except Exception as e:
        return {'error': str(e)}
    
#===================================================================================================================


@router.post("/handle-payment")
async def process_payment(payment_form: Payment, session: DBSESSION):
    session.add(payment_form)
    session.commit()
    session.refresh(payment_form)
    return payment_form

#=============================================================================================


@router.get('/customer-payments/{customer_id}')
async def get_customer_payments(customer_id: str):
    try:
        payments = stripe.PaymentIntent.list(customer=customer_id)
        return payments
    except Exception as e:
        return {'error': str(e)}
    
#=============================================================================================