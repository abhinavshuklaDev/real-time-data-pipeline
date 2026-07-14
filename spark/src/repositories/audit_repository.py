from pyspark.sql import SparkSession

from src.config import Config


class AuditRepository:

    @staticmethod
    def write(spark: SparkSession, df):

        (
            df.write
            .mode("append")
            .parquet(
                Config.AUDIT_PATH
            )
        )