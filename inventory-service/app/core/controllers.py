from app.core.crud import add_product
from app.models import Product
from app.settings import ADMIN_KEY
from app.db import get_session


def verify_admin_key(key: str):
    return key == ADMIN_KEY


def add_in_db(data):
    with next(get_session()) as session:
        product = Product(
            name=data.name,
            price=data.price,
            description=data.description,
            category_id=data.category_id,
        )
        add_product(session=session, product=product)
        return product