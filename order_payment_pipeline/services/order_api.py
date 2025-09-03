from fastapi import FastAPI
from common.models import Order
from common.kafka_producer import send_message

app = FastAPI()


@app.post("/orders/")
def create_order(order: Order):
    send_message("orders", order.dict())
    return {"status": "Order sent to Kafka", "order": order}
