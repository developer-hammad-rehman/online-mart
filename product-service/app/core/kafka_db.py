from fastapi import Depends
from app.core.crud import create_item
from app.db import Session ,engine
from app.models import Item


def add_in_db(item):
 with Session(engine) as session:
    item = Item(
        name=item.name,
        price=item.price,
        description=item.description,
        category_id=item.category_id,
    )
    print(item.model_dump())
    create_item(item , session)
    return item