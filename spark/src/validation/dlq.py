from src.config import Config


class DLQWriter:

    @staticmethod
    def write(df):

        return (

            df

            .writeStream

            .format("parquet")

            .outputMode("append")

            .option(
                "path",
                Config.DLQ_PATH
            )

            .option(
                "checkpointLocation",
                Config.DLQ_CHECKPOINT
            )

            .start()

        )