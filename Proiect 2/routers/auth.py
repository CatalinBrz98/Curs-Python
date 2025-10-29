from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from db import create_session
from dependencies import auth_user
from schemas import UserLogin, UserRegister
from models import UserModel
from dependencies import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/register')
def register(new_user: UserRegister, db: Session = Depends(create_session)):
    existing_user = db.query(UserModel).filter(UserModel.username == new_user.username).first()

    if existing_user is not None:
        raise HTTPException(status_code=422, detail="Username already registered")

    hashed_password = hash_password(new_user.password)
    user = UserModel(username=new_user.username, email=new_user.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    return {"status": "Success"}


@router.post('/login')
def login(login_user: UserLogin, db: Session = Depends(create_session)):
    if not auth_user(login_user, db):
        raise HTTPException(status_code=401, detail="Wrong user details")
    return {"status": "Success"}
