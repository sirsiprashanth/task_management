import string
from typing import List, Optional
import pydantic
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class UserRoles(str, Enum):
    User = "User"
    Admin = 'Admin'
    SuperAdmin = 'SuperAdmin'


class Users(BaseModel):
    username: str = Field(max_length=50)
    email_Id: EmailStr
    mobile: Optional[int]
    password: str
    provider: str
    role : UserRoles = 'User'
    status : Optional[str] = "APPROVED"

    @pydantic.validator('status')
    @classmethod
    def status_type_validation(cls, _status):
        allStatus = ["APPROVED", "REJECTED"]
        if not _status:
            return None
        if _status not in allStatus:
            raise ValueError(f'Status must be from {allStatus}')
        return _status

    @pydantic.validator('username')
    @classmethod
    def validate_user(cls, usr_name):
        if len(usr_name) > 50:
            raise ValueError('user name cannot exceed 50 charecters')
        if any(char in usr_name for char in string.punctuation):
            raise ValueError('user name cannot contain special charecters')
        else:
            return usr_name
        
    @pydantic.validator('password')
    @classmethod
    def validate_password(cls, pw_val):
        if len(pw_val) < 6:
            raise ValueError('Password has to be a minimum of 6 charecters')
        else:
            if any(d.isdigit() for d in pw_val) and any(u.isupper() for u in pw_val) and any(l.islower() for l in pw_val) and (p in pw_val for p in string.punctuation):
                return pw_val
            else:
                raise ValueError ('Password must contain atleast one punctuation mark, one number, one lowercase alphabet & one upper case alphabet ')
            
        
            
class UserLogin(BaseModel):
    user_name   :   str
    password    :   str
            

class User_out(BaseModel):
    username    :   str
    email_Id    :   EmailStr
    role        :   UserRoles = 'User'
    status      :   Optional[str] = "APPROVED"

    class Config:
        orm_mode = True


class Users_List(BaseModel):
    results :   List[User_out] = []

    class Config:
        orm_mode = True
