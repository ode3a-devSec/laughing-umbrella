from kafka import KafkaConsumer
import json

# Connect to Kafka broker
consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="order_processor",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)


print("Processing incoming orders...")
for message in consumer:
    order = message.value
    print(f"Processing order: {order}")
