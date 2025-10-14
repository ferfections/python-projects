from confluent_kafka import Consumer, KafkaError
import json

# Configuración del consumidor
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'demo-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
topic = 'demo-topic'
consumer.subscribe([topic])

print("🟡 Esperando mensajes...")

while True:
    msg = consumer.poll(1.0)  # espera 1 segundo por mensaje

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"❌ Error: {msg.error()}")
            break

    data = json.loads(msg.value().decode('utf-8'))
    print(f"🔵 Recibido: {data}")

consumer.close()