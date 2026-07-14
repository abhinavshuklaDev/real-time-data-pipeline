from pyspark.sql.functions import col


class ValidationRules:

    @staticmethod
    def order_exists():

        return col("order_id").isNotNull()

    @staticmethod
    def customer_exists():

        return col("customer_name").isNotNull()

    @staticmethod
    def valid_price():

        return col("price") > 0

    @staticmethod
    def valid_quantity():

        return col("quantity") > 0