from pydantic import BaseModel, Field

class Order(BaseModel):
    product_name : str
    price : str
    username : str
    quantity : int
    delivery_charges : int = Field(default=70)


class OrderModelStatus(BaseModel):
    order_id : int
    username:str
    product_name:str
    quantity : int
    status:str = Field(default="pending")