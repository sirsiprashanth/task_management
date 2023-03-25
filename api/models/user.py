from .__init__ import Base, BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Enum
from passlib import hash as _hash


class User(Base, BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    mobile = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=False)
    blocked = Column(Boolean, server_default="FALSE", nullable=False)
    provider = Column(String, nullable=False)
    role = Column(String, Enum("SUPERUSER", "ADMIN", "USER",
                  name="role"), nullable=False, default="USER")
    status = Column(String, Enum("ACTIVE", "SUSPEND",
                    name="user_status"), nullable=False, default="ACTIVE")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)
