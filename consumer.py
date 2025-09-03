from kafka import KafkaConsumer

# Connect to Kafka broker
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group',
    enable_auto_commit=True
)

print("Listening for messages...")

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
