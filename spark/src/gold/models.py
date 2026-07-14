from dataclasses import dataclass

from pyspark.sql import DataFrame


@dataclass
class GoldOutput:

    daily: DataFrame

    city: DataFrame

    product: DataFrame

    category: DataFrame

    customer: DataFrame

    source: DataFrame