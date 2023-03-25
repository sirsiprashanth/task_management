from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config import settings
import jwt
from database_config import get_db
from models.user import User


oauth2schema = OAuth2PasswordBearer("auth/swagger_login")

ALGORITHM = "HS256"


async def createToken(user: User):
    token = jwt.encode({
        "id": user.id,
    }, settings.AUTH_JWT_SECRET)
    return token


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2schema)):
    try:
        payload = jwt.decode(
            token, settings.AUTH_JWT_SECRET, ALGORITHM)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization token")
    else:
        user = db.query(User).get(payload["id"])
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Authenticated user not found")
        return user
