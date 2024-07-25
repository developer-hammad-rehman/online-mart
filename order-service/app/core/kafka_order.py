from typing import Literal
from sqlmodel import Session, select
from app.models import CompletedOrder, OrderStatus, PendingOrder
from app.db import get_session


def completed_order(
    order_id: int, username: str, product_name: str, quantity: int, session: Session
):
    order = CompletedOrder(
        order_id=order_id,
        username=username,
        product_name=product_name,
        quantity=quantity,
    )
    session.add(order)
    session.commit()
    session.refresh(order)


def pending_order(
    order_id: int, username: str, product_name: str, quantity: int, session: Session
):
    order = PendingOrder(
        order_id=order_id,
        username=username,
        product_name=product_name,
        quantity=quantity,
    )
    session.add(order)
    session.commit()
    session.refresh(order)


def place_order_stautus(
    status: Literal["pending", "arrived"], order_id: int, session: Session
):
    order_status = OrderStatus(status=status, order_id=order_id)
    session.add(order_status)
    session.commit()
    session.refresh(order_status)


def delete_pending_order(order_id: int, session: Session):
    order = session.exec(
        select(PendingOrder).where(PendingOrder.order_id == order_id)
    ).first()
    session.delete(order)
    session.commit()


def kafka_order_status(order_status: dict):
    with next(get_session()) as session:
        if order_status["status"] == "complete":
            place_order_stautus(
                status="arrived", order_id=order_status["order_id"], session=session
            )
            completed_order(
                order_status["order_id"],
                order_status["username"],
                order_status["product_name"],
                order_status["quantity"],
                session=session,
            )
            delete_pending_order(order_status["order_id"], session=session)
        else:
            place_order_stautus(
                status="pending", order_id=order_status["order_id"], session=session
            )
            pending_order(
                order_status["order_id"],
                order_status["username"],
                order_status["product_name"],
                order_status["quantity"],
                session=session,
            )
