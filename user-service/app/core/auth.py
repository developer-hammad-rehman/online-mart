from sqlmodel import Session, select
from passlib.context import CryptContext
from app.models import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username:str , password:str , session:Session) -> Users | None:
    statment = select(Users).where(username == Users.username)
    result = session.exec(statment).first()
    if result:
     is_password_valid = verify_password(password, result.password)
     if is_password_valid:
        return result
     else:
        return None
    else:
       return None
    


def get_user_by_username(username:str, session:Session) -> Users | None:
    statment = select(Users).where(username == Users.username)
    result = session.exec(statment).first()
    if result:
        return result
    else:
        return None