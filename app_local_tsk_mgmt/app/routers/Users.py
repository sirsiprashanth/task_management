
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy import func
from database import get_db
from sqlalchemy.orm import Session
from models import User
from schemas import Users, User_out, Users_List
from utils import pwd_hashing


router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=Users_List)
def get_all_user(db : Session = Depends(get_db)):
    all_users = db.query(User).all()
    return {"results": all_users}

@router.get('/{username}', response_model=User_out)
def get_user_name(username , db: Session = Depends(get_db)):
    user_data = db.query(User).filter(func.lower(User.username) == func.lower(username)).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail = f"User with user name '{username}' not found")
    else:
        return user_data
        


@router.post('/', response_model=User_out)
def create_user(user_data : Users,  db : Session = Depends(get_db)):
    hashed_pw = pwd_hashing(user_data.password)
    user_data.password = hashed_pw
    new_user = User(**dict(user_data))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete('/{username}', status_code=status.HTTP_200_OK)
def delete_user(username, db: Session = Depends(get_db)):
    user = db.query(User).filter(func.lower(username) == func.lower(User.username)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"User with user name '{username}' not found")
        
    else:
        db.delete(user)
        db.commit()
        return {f"User with user name '{username}' deleted"}
    

















































