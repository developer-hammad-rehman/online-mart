from typing import Optional

from sqlmodel import Session
from app.api.deps import FORMDEPS , DB_SESSION , PRODUCERDEPS
from fastapi import APIRouter, Depends, Form
from app.core.auth import get_user
from fastapi import HTTPException
from datetime import datetime , timedelta , timezone
from app.core.token import create_acces_token , create_refresh_token  , decode_token
from app.models import GPToken, Token
from app.settings import KAFKA_NOTIFICATION_TOPIC
from app.db import get_session
import json
from app.core.crud import get_kid

login_router = APIRouter(tags=["Auth Routes"])

@login_router.post("/login")
async def login(form_data: FORMDEPS , session:DB_SESSION , producer:PRODUCERDEPS):
    user = get_user(username=form_data.username, password=form_data.password, session=session)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    else:
        await producer.send_and_wait(KAFKA_NOTIFICATION_TOPIC , json.dumps({"type":"login" ,"email":form_data.username}).encode("utf-8"))
        expire_in = datetime.now(timezone.utc) + timedelta(days=1)
        access_token = create_acces_token(sub={"username":user.username , "k_id":user.k_id , "exp":expire_in})
        refresh_token = create_refresh_token(sub={"username":user.username})
        return GPToken(access_token=access_token, refresh_token=refresh_token, expires_in=36000)
    

@login_router.post("/oauth-token")
def oauth_token_route(grant_type: str = Form(...), refresh_token: Optional[str] = Form(None), code: Optional[str] = Form(None) , session : Session = Depends(get_session)):
   if grant_type == "refresh_token" and refresh_token:
           payload = decode_token(token=refresh_token)
           username = payload.get("username")
           k_id = get_kid(username=username , session=session)
           expire_in = datetime.now(timezone.utc) + timedelta(days=1)
           accces_token = create_acces_token(sub={"username":username , "exp" : expire_in , "k_id":k_id})
           new_refresh_token = create_refresh_token(sub={"username":username})
           return GPToken(access_token=accces_token,expires_in=expire_in.second , refresh_token=new_refresh_token)
   elif grant_type == "authorization_code" and code:
           payload = decode_token(token=code)
           username = payload.get("username")
           k_id = get_kid(username=username , session=session)
           accces_token = create_acces_token(sub={"username":username , "exp" : 36000 , "k_id":k_id})
           new_refresh_token = create_refresh_token(sub={"username":username})
           return GPToken(access_token=accces_token,expires_in=36000 , refresh_token=new_refresh_token)
   else:
       raise HTTPException(status_code=400, detail="Invalid grant type or token")