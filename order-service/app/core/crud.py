from sqlmodel import select  , Session
from app.models import Order


def place_order(order:Order , session:Session):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def delete_order(order_id:int, session:Session):
    order = session.get(Order, order_id)
    session.delete(order)
    session.commit()
    return {"message":"Order Deleted"}


def get_order_userorder(username:str, session:Session):
    order = session.exec(select(Order).where(Order.username == username)).all()
    return order

def get_all_orders(session:Session):
    statement = select(Order)
    orders = session.exec(statement).all()
    return orders