from typing import Literal, Optional
from sqlmodel import SQLModel , Field
from datetime import datetime


class Order(SQLModel , table=True):
    id : Optional[int] = Field(default=None , primary_key=True)
    product_name : str
    price : str
    username : str
    quantity : int
    created_at : datetime = Field(default=datetime.now())
    delivery_charges : int = Field(default=70)



class ApproveOrder(SQLModel , table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    des:str
    order_id : Optional[int] = Field(default=None , foreign_key="order.id")


class OrderStatus(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    status : str = Field(default="pending")
    order_id : Optional[int] = Field(default=None, foreign_key="order.id")



class PendingOrder(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    username:str
    product_name : str
    quantity : int
    order_id : int



class CompletedOrder(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    username:str
    product_name : str
    quantity : int
    order_id : int


class OrderModelStatus(SQLModel):
    order_id : int
    username:str
    product_name:str
    quantity : int
    status:str = Field(default="pending")