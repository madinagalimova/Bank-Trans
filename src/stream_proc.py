import asyncio
import json
from aiokafka import AIOKafkaConsumer
from models import Transaction

BOOTSTRAP_SERVERS = [
    'localhost:19092',
    'localhost:10092',
    'localhost:11092',
]

TOPIC = "transactions"


async def main():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id="mvp-consumer-group",
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )

    await consumer.start()
    print(f"Subscribed to topic: {TOPIC}")
    try:
        async for msg in consumer:
            try:
                raw_json = msg.value.decode("utf-8")
                tx = Transaction.model_validate_json(raw_json)
                print("Processed:", tx.model_dump())

                # сюда потом rule engine + запись в БД
            except Exception as e:
                print(f"Failed to parse message: {e}")
    finally:
        await consumer.stop()


if __name__ == "__main__":
    asyncio.run(main())
