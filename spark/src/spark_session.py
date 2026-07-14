from pyspark.sql import SparkSession

from src.config import Config


def create_spark():

    spark = (

        SparkSession.builder

        .master(Config.SPARK_MASTER)

        .appName(Config.APP_NAME)

        .config(
            "spark.sql.shuffle.partitions",
            str(Config.SPARK_SHUFFLE_PARTITIONS)
        )

        .config(
            "spark.sql.streaming.forceDeleteTempCheckpointLocation",
            "true"
        )

        .config(
            "spark.sql.session.timeZone",
            Config.SPARK_TIMEZONE
        )

        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0"
        )
    
        .getOrCreate()

    )

    spark.sparkContext.setLogLevel("WARN")

    return spark