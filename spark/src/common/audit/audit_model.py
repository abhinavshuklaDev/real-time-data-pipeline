from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class AuditRecord:

    pipeline: str

    status: str

    execution_date: date

    records_processed: int

    start_time: datetime

    end_time: datetime

    duration_seconds: float

    error_message: str | None = None