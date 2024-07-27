from fastapi import APIRouter
from app.api.deps import DBSESSION, PRODUCERDEP
from app.settings import KAFKA_TOPIC, KAFKA_NOTIFICATION_TOPIC
from app.core.crud import get_order_userorder, delete_order, place_order
from app.models import Order, OrderModelStatus
import json
from app import order_pb2

user_router = APIRouter(tags=["User Routes"])


@user_router.post("/place-order")
async def place_order_route(order: Order, session: DBSESSION, producer: PRODUCERDEP):
    
    await producer.send_and_wait(
        KAFKA_NOTIFICATION_TOPIC,
        json.dumps({"type": "order_placed", "email": order.username}).encode("utf-8"),
    )
    return place_order(order, session)


@user_router.get("/get-orders")
def get_order(username: str, session: DBSESSION):
    orders = get_order_userorder(username, session)
    return orders


@user_router.delete("/delete-order")
def delete_order_route(order_id: int, session: DBSESSION):
    return delete_order(order_id, session)


@user_router.post("/complete-order")
async def complete_order_route(order_status: OrderModelStatus, producer: PRODUCERDEP):
    protobuf = order_pb2.Order(order_id = order_status.order_id ,username=order_status.username ,product_name=order_status.product_name,quantity=order_status.quantity ,status=order_status.status) # type: ignore
    encoded_string = protobuf.SerializeToString()
    await producer.send_and_wait(
        KAFKA_TOPIC, 
        encoded_string
    )
    await producer.send_and_wait(
        KAFKA_NOTIFICATION_TOPIC,
        json.dumps({"type": "order_completed", "email": order_status.username}).encode(
            "utf-8"
        ),
    )
    return {"message": "Order completed"}
