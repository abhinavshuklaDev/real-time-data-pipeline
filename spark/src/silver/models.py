from dataclasses import dataclass

from pyspark.sql import DataFrame


@dataclass
class SilverOutput:

    silver: DataFrame