from src.spark_session import create_spark

from src.common.logger import get_logger


class BaseJob:

    def __init__(self):

        self.logger = get_logger(

            self.__class__.__name__

        )

        self.spark = create_spark()

    def stop(self):

        self.logger.info(

            "Stopping Spark Session"

        )

        self.spark.stop()