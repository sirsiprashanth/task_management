from database import Base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, Enum
from datetime import datetime

class BaseModel:
    deleted: bool = Column(Boolean, server_default="FALSE", nullable=False)
    created_at: DateTime = Column(DateTime, default=datetime.now)
    updated_at: DateTime = Column(
        DateTime, default=datetime.now, onupdate=datetime.now)


class User(Base, BaseModel):
    __tablename__ = 'users'
    id          =   Column(Integer, primary_key = True, unique = True, index = True)
    username    =   Column(String, unique = True)
    email_Id    =   Column(String, unique = True)
    mobile      =   Column(String, unique = False, nullable = True) 
    password    =   Column(String, nullable = True)
    blocked     =   Column(Boolean, default = False)
    provider    =   Column(String, nullable = False)
    role        =   Column(String, Enum("User", "Admin", "SuperAdmin", name="role"), nullable=False, default="User")
    status      =   Column(String, nullable = True)
    deleted     =   Column(Boolean, nullable = False, server_default = 'False')
    created_at  =   Column(DateTime, default=datetime.now)
    updated_at  =   Column(DateTime,default=datetime.now, onupdate=datetime.now)