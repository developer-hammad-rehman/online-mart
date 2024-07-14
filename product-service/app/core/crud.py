from sqlmodel import Session, select
from app.models import Category , AvaliableStock , HotItem ,SellItem  , Item


def get_category(session:Session):
    statement = select(Category)
    results = session.exec(statement)
    category = results.all()
    return category



def get_item(session:Session):
    statement = select(Item)
    results = session.exec(statement)
    item = results.all()
    return item



def get_avaliable_stock(session:Session):
    statement = select(AvaliableStock)
    results = session.exec(statement)
    avaliable_stock = results.all()
    return avaliable_stock


def get_hot_item(session:Session):
    statement = select(HotItem)
    results = session.exec(statement)
    hot_item = results.all()
    return hot_item


def get_sell_item(session:Session):
    statement = select(SellItem)
    results = session.exec(statement)
    sell_item = results.all()
    return sell_item


def create_category(session:Session,category:Category):
  statment = select(Category).where(Category.id == category.id)
  result = session.exec(statment).first()
  if not result:
    session.add(category)
    session.commit()
    session.refresh(category)
    return category
  return {"message":"Category already exists"}

def create_item(session:Session, item:Item):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def create_avaliable_stock(session:Session, avaliable_stock:AvaliableStock):
    session.add(avaliable_stock)
    session.commit()
    session.refresh(avaliable_stock)
    return avaliable_stock


def create_hot_item(session:Session, hot_item:HotItem):
    session.add(hot_item)
    session.commit()
    session.refresh(hot_item)
    return hot_item


def create_sell_item(session:Session, sell_item:SellItem):
    session.add(sell_item)
    session.commit()
    session.refresh(sell_item)
    return sell_item