from pydantic import BaseModel


class Order(BaseModel):
    order_id: int
    item: str


class Payment(BaseModel):
    order_id: int
    amount: float
