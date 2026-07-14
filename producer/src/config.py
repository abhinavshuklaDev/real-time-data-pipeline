from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")


class Config:

    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP")

    TOPIC_NAME = os.getenv("KAFKA_TOPIC")

    CLIENT_ID = os.getenv("KAFKA_CLIENT_ID")