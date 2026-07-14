from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
    TimestampType
)

ORDER_SCHEMA = StructType([

    StructField("order_id", IntegerType(), False),

    StructField("customer_id", IntegerType(), False),

    StructField("customer_name", StringType(), False),

    StructField("city", StringType(), True),

    StructField("product_id", IntegerType(), False),

    StructField("product_name", StringType(), False),

    StructField("category", StringType(), True),

    StructField("price", DoubleType(), False),

    StructField("discount", DoubleType(), True),

    StructField("quantity", IntegerType(), False),

    StructField("payment_method", StringType(), True),

    StructField("order_status", StringType(), True),

    StructField("event_time", StringType(), False)

])