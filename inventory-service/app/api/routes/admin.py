from fastapi import APIRouter

from app.api.deps import DBSESSIONDEPS
from app.core.crud import add_stock, get_stock, remove_stock
from app.models import Product


admin_router = APIRouter(tags=["Admin Routes"])

@admin_router.post("/add-stock")
def add_stock_route(stock:Product , session:DBSESSIONDEPS):
    result = add_stock(session=session , stock=stock)
    return result


@admin_router.get('/get-stocks')
def get_stocks_route(session:DBSESSIONDEPS):
    result = get_stock(session=session)
    return result



@admin_router.delete('/delete-stock')
def delete_stock_route(id:int, session:DBSESSIONDEPS):
    result = remove_stock(session=session, id=id)
    return result