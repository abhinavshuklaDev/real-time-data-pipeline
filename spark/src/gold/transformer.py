from pyspark.sql.functions import (
    sum,
    to_date,
    col
)
from src.gold.models import GoldOutput

class GoldTransformer:

    @staticmethod
    def transform(df):

        df.cache()

        daily_df = (

            df

            .withColumn(
                "order_date",
                to_date("event_time")
            )

            .groupBy(
                "order_date"
            )

            .agg(

                sum(
                    "total_amount"
                ).alias(
                    "daily_revenue"
                )

            )

        )

        city_df = (

            df

            .groupBy(
                "city"
            )

            .agg(

                sum(
                    "total_amount"
                ).alias(
                    "revenue"
                )

            )

            .orderBy(
                col("revenue").desc()
            )

        )

        product_df = (

            df

            .groupBy(
                "product_name"
            )

            .agg(

                sum(
                    "quantity"
                ).alias(
                    "units_sold"
                ),

                sum(
                    "total_amount"
                ).alias(
                    "revenue"
                )

            )

            .orderBy(
                col("revenue").desc()
            )

        )

        category_df = (

            df

            .groupBy(
                "category"
            )

            .agg(

                sum(
                    "total_amount"
                ).alias(
                    "revenue"
                )

            )

        )

        customer_df = (

            df

            .groupBy(
                "customer_name"
            )

            .agg(

                sum(
                    "total_amount"
                ).alias(
                    "spent"
                )

            )

            .orderBy(
                col("spent").desc()
            )

        )

        return GoldOutput(

            daily=daily_df,

            city=city_df,

            product=product_df,

            category=category_df,

            customer=customer_df,

            source=df

        )