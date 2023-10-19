from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, mapped_column
)
from .time_stamp import TimestampModel


class Todo(TimestampModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(30))

