from kafka import KafkaConsumer
import json

orders = {}
payments = {}

consumer = KafkaConsumer(
    "orders",
    "payments",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="order_payment_service",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)


print("Listening for orders and payments...")

for msg in consumer:
    data = msg.value
    if msg.topic == "orders":
        orders[data["order_id"]] = data
    elif msg.topic == "payments":
        payments[data["order_id"]] = data

    if data["order_id"] in orders and data["order_id"] in payments:
        print(
            f"Order completed: {orders[data['order_id']]} + {payments[data['order_id']]}"
        )
