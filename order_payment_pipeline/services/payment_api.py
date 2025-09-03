from fastapi import FastAPI
from common.models import Payment
from common.kafka_producer import send_message

app = FastAPI()


@app.post("/payments/")
def create_payment(payment: Payment):
    send_message("payments", payment.model_dump())
    return {"status": "Payment sent to Kafka", "payment": payment}
