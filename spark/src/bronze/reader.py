from src.repositories.kafka_repository import KafkaRepository
from src.config import Config


class BronzeReader:

    repository = KafkaRepository()

    @classmethod
    def read(

        cls,

        spark

    ):

        return cls.repository.read(

            spark,

            Config.KAFKA_BOOTSTRAP,

            Config.ORDERS_TOPIC

        )