from fastapi import APIRouter
from app.models import UpdateUser , UpdatePassword
from app.api.deps import DB_SESSION
from app.core.crud import update_password, update_username , delete_user
from fastapi import HTTPException

auth_crud = APIRouter(tags=["Auth Routes"])

@auth_crud.patch('/update-username')
def update_username_route(user_data:UpdateUser , session:DB_SESSION):
    user = update_username(username=user_data.username, session=session, password=user_data.password , new_username=user_data.new_username) # type: ignore
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    else:
        return {"message":user}
    

@auth_crud.patch('/forgot-password')
def update_password_route(user_data:UpdatePassword ,  session:DB_SESSION):
    user = update_password(username=user_data.username, session=session, new_password=user_data.new_password) 
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    return {"message":"Password updated successfully"}


@auth_crud.delete('/delete-account')
def delete_account_route(username:str ,session:DB_SESSION):
    user = delete_user(username=username, session=session)
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    return {"message":"Account deleted successfully"}