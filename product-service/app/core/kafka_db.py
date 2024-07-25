from app.core.crud import create_item
from app.db import  get_session
from app.models import Item


def add_in_db(item):
 with next(get_session()) as session:
    item = Item(
        name=item.name,
        price=item.price,
        description=item.description,
        category_id=item.category_id,
    )
    print(item.model_dump())
    create_item(item , session)
    return item