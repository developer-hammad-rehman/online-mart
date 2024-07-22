from typing import Optional
from sqlmodel import SQLModel , Field


class Payment(SQLModel  , table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    currency: str
    order_id: str
    type : str = Field(default="card")


class PaymentForm(SQLModel):
    amount: int
    payment_id : str



class PaymentIntents(SQLModel , table=True):
    id: int = Field(default=None, primary_key=True)
    amount: int
    currency: str
    payment_id: str
    payment_intent_id : str
    status: str