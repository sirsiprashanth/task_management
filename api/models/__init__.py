from .user import *
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean
from database_config import Base


class BaseModel:
    deleted: bool = Column(Boolean, server_default="FALSE", nullable=False)
    created_at: DateTime = Column(
        DateTime, default=datetime.now, nullable=False)
    updated_at: DateTime = Column(
        DateTime, default=datetime.now, nullable=False, onupdate=datetime.now)
