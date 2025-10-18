from confluent_kafka import Producer
import json
import time

# Configuración del productor
conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)
topic = 'demo-topic'


def delivery_report(err, msg):
    """Se llama cuando el mensaje se entrega (o falla)."""
    if err is not None:
        print(f"❌ Error al enviar mensaje: {err}")
    else:
        print(f"✅ Mensaje entregado a {msg.topic()} [{msg.partition()}]")

# Enviar algunos mensajes
for i in range(5):
    data = {'mensaje': f'Hola Kafka #{i}'}
    producer.produce(
        topic,
        key=str(i),
        value=json.dumps(data),
        callback=delivery_report
    )
    producer.poll(0)  # obliga a procesar callbacks
    time.sleep(1)

producer.flush()  # espera a que se envíen todos los mensajes