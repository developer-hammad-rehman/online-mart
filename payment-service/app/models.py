from sqlmodel import SQLModel , Field


class Payment(SQLModel  , table=True):
    id: int = Field(default=None, primary_key=True)
    amount: float
    currency: str
    status: str



class PaymentForm(SQLModel):
    amount: int