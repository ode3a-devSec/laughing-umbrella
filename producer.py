from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import uuid


app = FastAPI()

# Connect to Kafka broker
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


class Order(BaseModel):
    customer: str
    amount: float
    item: str


@app.post("/order")
async def create_order(order: Order):
    order_data = {
        "order_id": str(uuid.uuid4()),
        "customer": order.customer,
        "amount": order.amount,
        "item": order.item,
    }
    producer.send("orders", value=order_data)
    producer.flush()
    return {"message": "Order sent to Kafka", "order": order_data}
