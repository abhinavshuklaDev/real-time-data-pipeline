from pyspark.sql.functions import (
    current_timestamp,
    col
)

from src.silver.models import SilverOutput


class SilverTransformer:

    @staticmethod
    def transform(df):

        silver = (

            df

            .dropDuplicates(["order_id"])

            .withColumn(
                "total_amount",
                (col("price") - col("discount")) * col("quantity")
            )

            .withColumn(
                "processed_at",
                current_timestamp()
            )

        )

        return SilverOutput(
            silver=silver
        )