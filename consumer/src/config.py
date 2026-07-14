from dotenv import load_dotenv
import os

load_dotenv("../config/.env")


class Config:

    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
    TOPIC_NAME = os.getenv("TOPIC_NAME")
    GROUP_ID = os.getenv("GROUP_ID")
    AUTO_OFFSET_RESET = os.getenv("AUTO_OFFSET_RESET")