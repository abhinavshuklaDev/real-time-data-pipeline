from faker import Faker
from random import choice, randint
from datetime import datetime

from src.models import Order


fake = Faker("en_IN")


PRODUCTS = [

    (101, "MacBook Air", "Laptop", 125000),

    (102, "iPhone 17", "Mobile", 90000),

    (103, "Samsung TV", "Electronics", 55000),

    (104, "Sony Headphones", "Accessories", 12000),

    (105, "Mechanical Keyboard", "Accessories", 6000),

    (106, "Gaming Mouse", "Accessories", 3500)

]


PAYMENTS = [

    "UPI",

    "Credit Card",

    "Debit Card",

    "Net Banking"

]


class OrderGenerator:

    def generate_order(self):

        product = choice(PRODUCTS)

        price = float(product[3])

        discount = round(price * randint(0, 20) / 100, 2)

        return Order(

            order_id=randint(100000, 999999),

            customer_id=randint(1000, 9999),

            customer_name=fake.name(),

            city=fake.city(),

            product_id=product[0],

            product_name=product[1],

            category=product[2],

            price=price,

            discount=discount,

            quantity=randint(1, 5),

            payment_method=choice(PAYMENTS),

            order_status="PLACED",

            event_time=datetime.utcnow().isoformat()

        )