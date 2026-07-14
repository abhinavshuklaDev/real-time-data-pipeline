from src.repositories.base_repository import BaseRepository


class ParquetRepository(BaseRepository):

    def read(self, spark, path):

        return (

            spark.read

            .parquet(path)

        )

    def write(  

        self,

        df,

        path,

        mode="overwrite",

        partition_by=None

    ):

        writer = (

            df.write

            .mode(mode)

            .format("parquet")

        )

        if partition_by:

            writer = writer.partitionBy(

                *partition_by

            )

        writer.save(path)