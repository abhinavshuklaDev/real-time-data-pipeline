from pyspark.sql.functions import (
    when,
    lit,
    col
)


class Validator:

    @staticmethod
    def validate(df):

        return (

            df

            .withColumn(

                "failure_reason",

                when(
                    col("order_id").isNull(),
                    lit("Missing Order ID")
                )

                .when(
                    col("customer_name").isNull(),
                    lit("Missing Customer")
                )

                .when(
                    col("price") <= 0,
                    lit("Invalid Price")
                )

                .when(
                    col("quantity") <= 0,
                    lit("Invalid Quantity")
                )

            )

            .withColumn(

                "is_valid",

                col("failure_reason").isNull()

            )

        )

    @staticmethod
    def split(df):

        good = df.filter(col("is_valid"))

        bad = df.filter(~col("is_valid"))

        return good, bad