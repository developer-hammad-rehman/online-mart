from sqlmodel import Session, select

from app.models import Inventory, Product, Record, Suppliers


def add_product(session:Session , product : Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product



def get_product(session:Session):
    result = session.exec(select(Product)).all()
    return result



def single_product(session:Session, id:int):
    result = session.get(Product, id)
    return result


def remove_product(session:Session, id:int):
    result = session.get(Product, id)
    session.delete(result)
    session.commit()
    return {"message": "Product removed successfully"}


def update_inventory(inventory:Inventory , session:Session):
    session.add(inventory)
    session.commit()
    session.refresh(inventory)
    return inventory

def get_inventory(session:Session):
    result = session.exec(select(Inventory)).all()
    return result


def add_supplier(supplier:Suppliers , session:Session):
    session.add(supplier)
    session.commit()
    session.refresh(supplier)
    return supplier


def get_suppliers(session:Session):
    result = session.exec(select(Suppliers)).all()
    return result


def update_record(record:Record , session:Session):
    session.add(record)
    session.commit()
    session.refresh(record)

def get_records(session:Session):
    result = session.exec(select(Record)).all()
    return result


def get_record_product(product_id:int , session:Session):
    result = session.exec(select(Record).where(product_id == Record.product_id))
    return result