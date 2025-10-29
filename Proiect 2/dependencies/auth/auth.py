import bcrypt
from sqlalchemy.orm import Session

from models import UserModel
from schemas import UserLogin


def hash_password(password: str) -> str:
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode('utf-8')


def check_password(password: str, hashed_password: str) -> bool:
    password = password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)


def auth_user(user: UserLogin, db: Session) -> bool:
    existing_user: UserModel | None = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user is None or not check_password(user.password, existing_user.hashed_password):
        return False
    return True
