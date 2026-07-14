from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os


BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")

DATA_DIR = BASE_DIR / "data"

@dataclass(frozen=True)
class Config:

    APP_NAME = os.getenv("APP_NAME")

    SPARK_MASTER = os.getenv("SPARK_MASTER")

    SPARK_TIMEZONE = os.getenv("SPARK_TIMEZONE")

    SPARK_SHUFFLE_PARTITIONS = int(
        os.getenv("SPARK_SHUFFLE_PARTITIONS")
    )

    KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")

    ORDERS_TOPIC = os.getenv("KAFKA_TOPIC")

    BRONZE_PATH = str(DATA_DIR / "bronze" / "orders")

    BRONZE_CHECKPOINT = str(DATA_DIR / "checkpoints" / "bronze")

    DLQ_PATH = str(DATA_DIR / "bronze" / "dlq")

    DLQ_CHECKPOINT = str(DATA_DIR / "checkpoints" / "dlq")

    SILVER_PATH = str(DATA_DIR / "silver" / "orders")

    GOLD_DAILY_REVENUE = str(DATA_DIR / "gold" / "daily_revenue")

    GOLD_CITY_SALES = str(DATA_DIR / "gold" / "city_sales")

    GOLD_PRODUCT_SALES = str(DATA_DIR / "gold" / "top_products")

    GOLD_CATEGORY_SALES = str(DATA_DIR / "gold" / "category_sales")

    GOLD_TOP_CUSTOMERS = str(DATA_DIR / "gold" / "top_customers")

    AUDIT_PATH = str(DATA_DIR / "audit")