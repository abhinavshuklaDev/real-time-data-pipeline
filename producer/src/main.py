import time

from src.order_generator import OrderGenerator
from src.producer import OrderProducer


generator = OrderGenerator()

producer = OrderProducer()


try:

    while True:

        order = generator.generate_order()

        producer.send(order)

        print(order)

        time.sleep(1)

except KeyboardInterrupt:

    print("\nStopping Producer...")

finally:

    producer.close()

    print("Producer Closed")