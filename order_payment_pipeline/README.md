# laughing-umbrella
Business flow:

FastAPI Producer 1: Accepts new orders and sends them to Kafka (orders topic).

FastAPI Producer 2: Accepts payment confirmations and sends them to Kafka (payments topic).

Consumer: Listens to both topics and links orders with payments to mark them as completed.