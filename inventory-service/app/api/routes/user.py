from fastapi import APIRouter
from app.core.crud import get_stock ,single_product
from app.api.deps import DBSESSIONDEPS , PRODUCERDEPS
from app.settings import KAFKA_TOPIC
from app.models import Product
import json

user_router = APIRouter(tags=["User Routes"])


@user_router.get('/get-stock')
def get_product_route(session:DBSESSIONDEPS):
    result = get_stock(session=session)
    return result



@user_router.get('/get-product/{id}')
def get_product(id:int ,session:DBSESSIONDEPS):
    result = single_product(id=id,session=session)
    return result



@user_router.post('/place-order')
async def place_order_route(product : Product  , username:str, producer:PRODUCERDEPS):
    order_product =  product.model_dump().copy()
    order_product.update({"username":username})
    await producer.send_and_wait(KAFKA_TOPIC , json.dumps(order_product).encode('utf-8'))
    return {"message": "Order placed successfully"}