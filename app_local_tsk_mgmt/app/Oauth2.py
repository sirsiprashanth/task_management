
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt
 
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = 'e7e71996fa66ad5cd1d4383b280cda264d400dd0d28a41ea02ea12a60803aaf3'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES =30
 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt