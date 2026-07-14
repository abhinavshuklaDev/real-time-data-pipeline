from pyspark.sql.functions import (
    col,
    from_json
)

from src.schema import ORDER_SCHEMA


class Parser:

    @staticmethod
    def parse(df):

        return (

            df

            .selectExpr(
                "CAST(value AS STRING) AS json"
            )

            .select(

                from_json(
                    col("json"),
                    ORDER_SCHEMA
                ).alias("data")

            )

            .select(
                "data.*"
            )

        )