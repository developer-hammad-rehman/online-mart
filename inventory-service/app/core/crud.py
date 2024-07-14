from sqlmodel import Session, select

from app.models import Product


def add_stock(session:Session , stock : Product):
    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock



def get_stock(session:Session):
    result = session.exec(select(Product)).all()
    return result



def single_product(session:Session, id:int):
    result = session.get(Product, id)
    return result


def remove_stock(session:Session, id:int):
    result = session.get(Product, id)
    session.delete(result)
    session.commit()
    return {"message": "Product removed successfully"}