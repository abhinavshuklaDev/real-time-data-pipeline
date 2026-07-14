from dataclasses import dataclass


@dataclass
class Order:

    order_id: int

    customer_id: int

    customer_name: str

    city: str

    product_id: int

    product_name: str

    category: str

    price: float

    discount: float

    quantity: int

    payment_method: str

    order_status: str

    event_time: str