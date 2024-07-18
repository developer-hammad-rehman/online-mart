from fastapi import APIRouter
import requests
from app.auth_config import TOKEN_DEPS
from app.models import Order, OrderModelStatus
from app.settings import ORDER_SERVICE_URL

order_router = APIRouter()


@order_router.post("/place-order")
async def place_order(order:Order , token:TOKEN_DEPS):
    response = requests.post(f"{ORDER_SERVICE_URL}/place-order", json=order.model_dump()).json()
    return response



@order_router.get("/get-orders")
async def get_order(email:str , token:TOKEN_DEPS):
    response = requests.get(f"{ORDER_SERVICE_URL}/get-orders?username={email}").json()
    return response


@order_router.delete("/delete-order/{order_id}")
async def delete_order(order_id:int , token:TOKEN_DEPS):
    response = requests.delete(f"{ORDER_SERVICE_URL}/delete-order/{order_id}").json()
    return response


@order_router.post("/complete-order")
async def complete_order(request:OrderModelStatus , token:TOKEN_DEPS):
    response = requests.post(f"{ORDER_SERVICE_URL}/complete-order" , json=request.model_dump()).json()
    return response