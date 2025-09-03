from kafka import KafkaProducer

# Connect to Kafka broker
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send 10 messages
for i in range(10):
    message = f"Message {i}".encode('utf-8')
    producer.send('test-topic', message)
    print(f"Sent: {message}")

# Ensure all messages are sent
producer.flush()
print("All messages sent!")
