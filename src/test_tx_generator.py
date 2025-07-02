import json
import uuid
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=[
    'localhost:19092',
    'localhost:10092',
    'localhost:11092',
    ],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

def gen_tx():
    return {
        "id": str(uuid.uuid4()),
        "amount": round(random.uniform(1, 1000), 2),
        "currency": "RUB",
        "timestamp": datetime.utcnow().isoformat(),
    }

if __name__ == "__main__":
    print("Start sending to topic 'transactions'…")
    while True:
        tx = gen_tx()
        producer.send("transactions", tx)
        print("→", tx)
        time.sleep(1)
