from app.core.auth import pwd_context , Users , get_user_by_username
from sqlmodel import Session, select

def add_user(username:str, password:str, session:Session) -> Users:
    hashed_password = pwd_context.hash(password)
    user = Users(username=username, password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_username(username:str , password:str , new_username:str , session:Session):
    statment = (select(Users).where(Users.username == username))
    user = session.exec(statment).first()
    is_new_username_exist = get_user_by_username(new_username, session)
    if not user:
        return None
    else:
        if not pwd_context.verify(password, user.password):
            return None
        else:
            if is_new_username_exist:
                return "Username Already Exist"
            user.username = new_username
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

def update_password(username:str, new_password:str, session:Session) -> Users|None:
    user = session.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return None
    user.password = pwd_context.hash(new_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(username:str, session:Session):
    user = session.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return False
    print(user)
    session.delete(user)
    session.commit()
    return True

def get_kid(session:Session, username:str):
    user = session.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return None
    return user.k_id