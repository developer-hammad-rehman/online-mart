from app.db_config import get_session , Session
from app.models import PaymentIntents
import stripe
from app.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY

def add_payment_intent(data):
    stripe_intent = stripe.PaymentIntent.retrieve(data.payment_intent_id)
    payment_intent = PaymentIntents(payment_id=data.payment_id , payment_intent_id=data.payment_intent_id , amount=stripe_intent.amount , currency=stripe_intent.currency , status=stripe_intent.status)
    session : Session = get_session() # type: ignore
    session.add(payment_intent)
    session.commit()
    session.refresh(payment_intent)
    return payment_intent.model_dump()