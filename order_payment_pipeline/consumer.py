from kafka import KafkaConsumer
import json

orders = {}
payments = {}

order_consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

payment_consumer = KafkaConsumer(
    "payments",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print("✅ Consumers running...")

while True:
    for msg in order_consumer.poll(timeout_ms=500).values():
        for record in msg:
            order = record.value
            orders[order["order_id"]] = order
            print("📦 Order received:", order)

    for msg in payment_consumer.poll(timeout_ms=500).values():
        for record in msg:
            payment = record.value
            payments[payment["order_id"]] = payment
            print("💰 Payment received:", payment)

    # Join orders + payments
    for oid in set(orders.keys()) & set(payments.keys()):
        print(f"✅ Matched Order {orders[oid]} with Payment {payments[oid]}")
