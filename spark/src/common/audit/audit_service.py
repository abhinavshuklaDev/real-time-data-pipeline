from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
    TimestampType,
    DateType
)
from datetime import datetime

from pyspark.sql import Row

from src.common.constants import PipelineStatus
from src.repositories.audit_repository import AuditRepository

AUDIT_SCHEMA = StructType([

    StructField(
        "pipeline",
        StringType(),
        False
    ),

    StructField(
        "status",
        StringType(),
        False
    ),

    StructField(
        "execution_date",
        DateType(),
        False
    ),

    StructField(
        "records_processed",
        IntegerType(),
        False
    ),

    StructField(
        "start_time",
        TimestampType(),
        False
    ),

    StructField(
        "end_time",
        TimestampType(),
        False
    ),

    StructField(
        "duration_seconds",
        DoubleType(),
        False
    ),

    StructField(
        "error_message",
        StringType(),
        True
    )

])

class AuditService:

    @staticmethod
    def success(

        spark,

        pipeline,

        records,

        start_time

    ):

        end_time = datetime.now()

        duration = (

            end_time - start_time

        ).total_seconds()

        row = Row(

            pipeline=pipeline,

            status=PipelineStatus.SUCCESS,

            execution_date=end_time.date(),

            records_processed=records,

            start_time=start_time,

            end_time=end_time,

            duration_seconds=duration,

            error_message=None

        )

        df = spark.createDataFrame(
            [row],
            schema=AUDIT_SCHEMA
        )

        AuditRepository.write(
            spark,
            df
        )

    @staticmethod
    def failure(

        spark,

        pipeline,

        start_time,

        error

    ):

        end_time = datetime.now()

        duration = (

            end_time - start_time

        ).total_seconds()

        row = Row(

            pipeline=pipeline,

            status=PipelineStatus.FAILED,

            execution_date=end_time.date(),

            records_processed=0,

            start_time=start_time,

            end_time=end_time,

            duration_seconds=duration,

            error_message=str(error)

        )

        df = spark.createDataFrame(
            [row],
            schema=AUDIT_SCHEMA
        )

        AuditRepository.write(
            spark,
            df
        )