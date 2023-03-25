from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy import func
from database import get_db
from sqlalchemy.orm import Session
from models import User
from utils import validate_pw, phone_otp_validate
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Oauth2 import create_access_token




router = APIRouter()


@router.post('/login', tags = ['User Authentication'])
def user_login(user_credentials : OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):

    user_login = db.query(User).filter(func.lower(User.username) == func.lower(user_credentials.username)).first()
    
    if not user_login:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Invalid credentials' )
    
    if not validate_pw(user_credentials.password, user_login.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Invalid credentials')
    else:
        print(f'mobile Num : {user_login.mobile}')
        result = phone_otp_validate(user_login.mobile)
        while result == 'approved':
            token =  create_access_token(data={'Sub' : user_login.username})
            return {'jwt' : token}
        
        

    


    