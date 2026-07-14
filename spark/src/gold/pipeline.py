from src.common.pipeline import Pipeline

from src.gold.reader import GoldReader
from src.gold.transformer import GoldTransformer
from src.gold.writer import GoldWriter

from src.config import Config


class GoldPipeline(Pipeline):

    def read(self):

        return GoldReader.read(self.spark)

    def transform(self, df):

        return GoldTransformer.transform(df)

    def write(self, output):

        GoldWriter.write(
            output.daily,
            Config.GOLD_DAILY_REVENUE
        )

        GoldWriter.write(
            output.city,
            Config.GOLD_CITY_SALES
        )

        GoldWriter.write(
            output.product,
            Config.GOLD_PRODUCT_SALES
        )

        GoldWriter.write(
            output.category,
            Config.GOLD_CATEGORY_SALES
        )

        GoldWriter.write(
            output.customer,
            Config.GOLD_TOP_CUSTOMERS
        )

        output.source.unpersist()

    def record_count(self, output):

        return output.source.count()
        