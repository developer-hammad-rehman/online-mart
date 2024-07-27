from fastapi import APIRouter
from sqlmodel import select
from app.api.deps import DBSESSION , PRODUCERDEP
from app.core.crud import get_all_orders
from app.models import Order , ApproveOrder , OrderModelStatus
from app.settings import KAFKA_TOPIC
from app import order_pb2

admin_router = APIRouter(tags=["Admin Routes"])


@admin_router.get("/admin" , response_model=list[Order])
def get_orders_router(session:DBSESSION):
    orders = get_all_orders(session)
    return orders


@admin_router.post('/approve-order' , response_model=ApproveOrder)
def approve_order_router(approve_order : ApproveOrder, session:DBSESSION , producer:PRODUCERDEP):
    session.add(approve_order)
    session.commit()
    session.refresh(approve_order)
    return approve_order


@admin_router.get('/get-approve-orders')
def get_approve_orders_router(session:DBSESSION):
     result = session.exec(select(ApproveOrder)).all()
     return result


@admin_router.post('/publish-order-status')
async def publish_order_status(order_status:OrderModelStatus, producer:PRODUCERDEP):
    protobuf = order_pb2.Order(order_id = order_status.order_id ,username=order_status.username ,product_name=order_status.product_name,quantity=order_status.quantity ,status=order_status.status) # type: ignore
    encoded_string = protobuf.SerializeToString()
    await producer.send_and_wait(
        KAFKA_TOPIC, 
        encoded_string
    )
    return {'status': 'Order status published successfully'}