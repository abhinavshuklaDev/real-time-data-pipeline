from src.repositories.parquet_repository import ParquetRepository


class GoldWriter:

    repository = ParquetRepository()

    @classmethod
    def write(
        cls,
        df,
        path
    ):
        cls.repository.write(
            df,
            path
        )