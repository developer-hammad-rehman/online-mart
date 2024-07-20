from fastapi import Depends
from sqlmodel import Session
from app.db_config import get_session
# from app.depends import DBSESSION 
from app.models import Payment



def add_in_db(data , session : Session = Depends(get_session)):
    payment = Payment(amount=data.amount, currency=data.curreny, status=data.status)
    session.add(payment)
    session.commit()
    session.refresh(payment)