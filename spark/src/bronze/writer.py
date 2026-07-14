from src.config import Config
from src.common.logger import get_logger


logger = get_logger(__name__)


class BronzeWriter:

    @staticmethod
    def write(df):

        logger.info("Starting Bronze Stream...")

        query = (
            df.writeStream
            .format("parquet")
            .outputMode("append")
            .option(
                "path",
                Config.BRONZE_PATH
            )
            .option(
                "checkpointLocation",
                Config.BRONZE_CHECKPOINT
            )
            .start()
        )

        logger.info("Bronze Stream Started")

        return query