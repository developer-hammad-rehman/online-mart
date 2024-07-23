from typing import Optional
from sqlmodel import SQLModel , Field


class Payment(SQLModel  , table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    currency: str
    status: str
    type : str = Field(default="card")