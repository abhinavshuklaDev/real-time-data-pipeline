import json

from confluent_kafka import Consumer

from src.config import Config


class OrderConsumer:

    def __init__(self):

        self.consumer = Consumer(
            {
                "bootstrap.servers": Config.BOOTSTRAP_SERVERS,
                "group.id": Config.GROUP_ID,
                "auto.offset.reset": Config.AUTO_OFFSET_RESET,
                "enable.auto.commit": False,
            }
        )

        self.consumer.subscribe([Config.TOPIC_NAME])

    def consume(self):

        while True:

            msg = self.consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                print(msg.error())
                continue

            order = json.loads(msg.value().decode())
            try:

                print(order)

                # Simulate database write
                # Simulate Spark write
                # Simulate API call

                self.consumer.commit(msg)

            except Exception as e:

                print(e)









