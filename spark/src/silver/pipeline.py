from src.common.pipeline import Pipeline
from src.silver.reader import SilverReader
from src.silver.transformer import SilverTransformer
from src.silver.writer import SilverWriter


class SilverPipeline(Pipeline):

    def read(self):

        return SilverReader.read(self.spark)

    def transform(self, df):

        return SilverTransformer.transform(df)

    def write(self, output):

        SilverWriter.write(
            output.silver
        )

    def record_count(self, output):

        return output.silver.count()    