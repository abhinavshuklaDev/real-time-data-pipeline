from src.repositories.parquet_repository import ParquetRepository
from src.config import Config


class SilverWriter:

    repository = ParquetRepository()

    @classmethod
    def write(cls, df):

        cls.repository.write(
            df,
            Config.SILVER_PATH
        )