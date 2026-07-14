from abc import ABC, abstractmethod
from datetime import datetime

from src.spark_session import create_spark
from src.common.logger import get_logger
from src.common.audit.audit_service import AuditService


class Pipeline(ABC):

    def __init__(self):

        self.spark = create_spark()

        self.logger = get_logger(
            self.__class__.__name__
        )

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def transform(self, df):
        pass

    @abstractmethod
    def write(self, output):
        pass

    def execute(self):

        start_time = datetime.now()

        try:

            self.logger.info("Reading")

            df = self.read()

            self.logger.info("Transforming")

            output = self.transform(df)

            self.logger.info("Writing")

            self.write(output)

            record_count = self.record_count(output)

            AuditService.success(

                spark=self.spark,

                pipeline=self.__class__.__name__,

                records=record_count,

                start_time=start_time

            )

        except Exception as e:

            self.logger.exception(e)

            AuditService.failure(

                spark=self.spark,

                pipeline=self.__class__.__name__,

                start_time=start_time,

                error=e

            )

            raise

        finally:

            self.logger.info(
                "Stopping Spark Session"
            )

            self.spark.stop()

    def record_count(self, output):

        return 0