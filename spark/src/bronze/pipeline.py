from src.common.pipeline import Pipeline

from src.bronze.reader import BronzeReader
from src.bronze.transformer import BronzeTransformer
from src.bronze.writer import BronzeWriter

from src.validation.dlq import DLQWriter


class BronzePipeline(Pipeline):

    def read(self):

        return BronzeReader.read(
            self.spark
        )

    def transform(self, df):

        return BronzeTransformer.transform(df)

    def write(self, output):

        BronzeWriter.write(
            output.bronze
        )

        DLQWriter.write(
            output.dlq
        )

        self.spark.streams.awaitAnyTermination()

    def record_count(self, output):

        return output.bronze.count()    