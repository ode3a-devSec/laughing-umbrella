from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json


app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


class Payment(BaseModel):
    order_id: str
    payment_method: str
    amount: float


@app.post("/payment")
async def confirm_payment(payment: Payment):
    payment_data = {
        "order_id": payment.order_id,
        "payment_method": payment.payment_method,
        "amount": payment.amount,
        "status": "PAID",
    }

    producer.send("payments", value=payment_data)
    producer.flush()
    return {"message": "Payment confirmed", "payment": payment_data}
