from src.repositories.base_repository import BaseRepository
from src.config import Config


class KafkaRepository(BaseRepository):

    def read(

        self,

        spark,

        bootstrap_servers,

        topic,

        starting_offsets="latest"

    ):

        return (
            spark.readStream
                .format("kafka")
                .option("kafka.bootstrap.servers", Config.KAFKA_BOOTSTRAP)
                .option("subscribe", Config.ORDERS_TOPIC)
                .option("startingOffsets", "latest")
                .option("failOnDataLoss", "false")
                .load()
        )

    def write(self, *args, **kwargs):

        raise NotImplementedError(

            "Kafka write is not implemented."

        )