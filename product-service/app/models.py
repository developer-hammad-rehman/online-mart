from typing import Literal
from sqlmodel import SQLModel , Field


class Category(SQLModel , table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str



class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    category_id: int = Field(foreign_key="category.id")



class AvaliableStock(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    quantity: int
    item_id: int = Field(foreign_key="item.id")



class SellItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    percent : int
    item_id: int = Field(foreign_key="item.id")


class HotItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    item_id: int = Field(foreign_key="item.id")