from src.repositories.parquet_repository import ParquetRepository
from src.config import Config


class GoldReader:

    repository = ParquetRepository()

    @classmethod
    def read(

        cls,

        spark

    ):

        return cls.repository.read(

            spark,

            Config.SILVER_PATH

        )