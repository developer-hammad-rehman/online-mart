from fastapi import APIRouter
from app.api.deps import DBSESSION
from app.core.crud import create_category , create_item , create_hot_item , create_avaliable_stock , create_sell_item
from app.models import Category, SellItem , HotItem ,AvaliableStock , Item

admin_router = APIRouter(tags=["Admin Routes"])


@admin_router.post("/add-category")
def add_category_route( category:Category,  session:DBSESSION):
    return create_category(category=category, session=session)


@admin_router.post('/add-item')
def add_item_route(item:Item, session:DBSESSION):
    return create_item(item=item, session=session)


@admin_router.post('/add-hot-item')
def add_hot_item_route(hot_item:HotItem, session:DBSESSION):
    return create_hot_item(hot_item=hot_item, session=session)


@admin_router.post('/add-avaliable-stock')
def add_avaliable_stock_route(avaliable_stock:AvaliableStock, session:DBSESSION):
    return create_avaliable_stock(avaliable_stock=avaliable_stock, session=session)

@admin_router.post('/add-sell-item')
def add_sell_item_route(sell_item:SellItem, session:DBSESSION):
    return create_sell_item(sell_item=sell_item, session=session)