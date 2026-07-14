from dataclasses import dataclass

from pyspark.sql import DataFrame


@dataclass
class BronzeOutput:

    bronze: DataFrame

    dlq: DataFrame
