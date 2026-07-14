import json
from dataclasses import asdict

from confluent_kafka import Producer

from src.config import Config


class OrderProducer:

    def __init__(self):

        self.producer = Producer(
            {
                "bootstrap.servers": Config.KAFKA_BOOTSTRAP_SERVERS,
                "client.id": Config.CLIENT_ID,

                # Reliability
                "acks": "all",
                "enable.idempotence": True,
                "retries": 10,

                # Performance
                "compression.type": "lz4",
                "linger.ms": 20,
                "batch.num.messages": 1000,
            }
        )
    def delivery_report(self, err, msg):

        if err is not None:
            print(f" Delivery Failed: {err}")

        else:
            print(
                f" Delivered "
                f"Topic={msg.topic()} "
                f"Partition={msg.partition()} "
                f"Offset={msg.offset()}"
            )

    def send(self, order):

        payload = json.dumps(asdict(order))

        self.producer.produce(
            topic=Config.TOPIC_NAME,
            value=payload,
            callback=self.delivery_report,
        )

        self.producer.poll(0)

    def close(self):

        self.producer.flush()

