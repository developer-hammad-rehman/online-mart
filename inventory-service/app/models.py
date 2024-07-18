from datetime import datetime
from sqlmodel import SQLModel , Field
from typing import Literal, Optional

class Category(SQLModel , table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str
    price : float
    description : str
    created_at : datetime = Field(default=datetime.now())
    category_id : Optional[int] = Field(default=None , foreign_key="category.id")


class Inventory(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    quantity  : int
    location : str
    updated_at: datetime = Field(default=datetime.now())
    product_id : Optional[int] = Field(default=None , foreign_key="product.id")


class Suppliers(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    name : str
    email : str
    ph_number:int
    product_name:str
    product_id : Optional[int] = Field(default=None , foreign_key="product.id")



class Record(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    product_id : Optional[int] = Field(default=None , primary_key=True)
    record_level : str
    supplier_id : Optional[int] = Field(default=None , foreign_key="suppliers.id")
    supplier_name:str