from fastapi import APIRouter
from app.api.deps import DBSESSION
from app.core.crud import get_category , get_item , get_avaliable_stock , get_hot_item ,  get_sell_item

user_router = APIRouter(tags=["User Routes"])

@user_router.get("/get-category")
def get_category_route(session:DBSESSION):
    category = get_category(session)
    return category


@user_router.get("/get-items")
def get_item_route(session:DBSESSION):
    item = get_item(session)
    return item


@user_router.get("/get-avaliable-items")
def get_avaliable_stock_route(session:DBSESSION):
    avaliable_stock = get_avaliable_stock(session)
    return avaliable_stock


@user_router.get("/get-hot-items")
def get_hot_item_route(session:DBSESSION):
    hot_item = get_hot_item(session)
    return hot_item

@user_router.get("/get-sell-items")
def get_sell_item_route(session:DBSESSION):
    sell_item = get_sell_item(session)
    return sell_item