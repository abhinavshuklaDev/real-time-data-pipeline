from src.repositories.parquet_repository import ParquetRepository

from src.config import Config


class SilverReader:

    repository = ParquetRepository()

    @classmethod
    def read(

        cls,

        spark

    ):

        return cls.repository.read(

            spark,

            Config.BRONZE_PATH

        )