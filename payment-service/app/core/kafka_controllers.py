from app.db_config import engine , Session
from app.models import Payment
import stripe
from app.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY

def add_payment(data):
    with Session(engine) as session:
        payment = Payment(amount=data.amount ,currency=data.currency , status=data.status ,type=data.type) 
        session.add(payment)
        session.commit()
        session.refresh(payment)
        return payment