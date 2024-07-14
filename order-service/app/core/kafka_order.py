from typing import Literal
from sqlmodel import Session, select
from app.models import CompletedOrder , OrderStatus , PendingOrder
from app.db import engine


def completed_order(order_id: int , username:str  ,product_name:str , quantity:int):
     with Session(engine) as session:
        order = CompletedOrder(order_id=order_id , username=username, product_name=product_name, quantity=quantity)
        session.add(order)
        session.commit()
        session.refresh(order)

def pending_order(order_id: int , username:str  ,product_name:str , quantity:int):
    with Session(engine) as session:
        order = PendingOrder(order_id=order_id, username=username, product_name=product_name, quantity=quantity)
        session.add(order)
        session.commit()
        session.refresh(order)

def place_order_stautus(status:Literal["pending" , "arrived"] , order_id:int):
    with Session(engine) as session:
        order_status = OrderStatus(status=status, order_id=order_id)
        session.add(order_status)
        session.commit()
        session.refresh(order_status)

def delete_pending_order(order_id:int):
    with Session(engine) as session:
        order = session.exec(select(PendingOrder).where(PendingOrder.order_id == order_id)).first()
        session.delete(order)
        session.commit()


def kafka_order_status(order_status : dict):
    if order_status["status"] == "complete":
        place_order_stautus(status="arrived" , order_id=order_status["order_id"])
        completed_order(order_status["order_id"], order_status["username"], order_status["product_name"], order_status["quantity"])
        delete_pending_order(order_status["order_id"])
    else:
        place_order_stautus(status="pending", order_id=order_status["order_id"])
        pending_order(order_status["order_id"], order_status["username"], order_status["product_name"], order_status["quantity"])