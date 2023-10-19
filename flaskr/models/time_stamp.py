from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import (
    Mapped, mapped_column
)

from flaskr.db import app_db


class TimestampModel(app_db.Model):
    __abstract__ = True
    created: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)