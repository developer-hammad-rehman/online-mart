from fastapi import APIRouter
from app.auth_config import TOKEN_DEPS
from app.settings import PRODUCT_SERVICE_URL
import requests

product_router = APIRouter()


@product_router.get("/get-category")
async def get_category(token:TOKEN_DEPS):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/get-category').json()
    return response


@product_router.get("/get-items")
async def get_items(token:TOKEN_DEPS):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/get-items').json()
    return response



@product_router.get("/get-avaliable-items")
async def get_avaliable_items(token:TOKEN_DEPS):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/get-avaliable-items').json()
    return response



@product_router.get("/get-hot-items")
async def get_hot_items(token:TOKEN_DEPS):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/get-hot-items').json()
    return response


@product_router.get("/get-sell-items")
async def get_sell_items(token:TOKEN_DEPS):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/get-sell-items').json()
    return response