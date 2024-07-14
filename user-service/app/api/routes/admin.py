from fastapi import APIRouter
from app.api.deps import FORMDEPS
from app.core.admin import verify_password , verify_username
from fastapi import HTTPException
from app.core.token import create_acces_token , create_refresh_token
from app.settings import ADMIN_KONG_ID
from datetime import timedelta , datetime , timezone
from app.models import Token

admin_router = APIRouter(tags=["Admin Routes"])


@admin_router.post('/admin-verify')
def login(formdata:FORMDEPS):
    is_username = verify_username(formdata.username)
    if not is_username:
        raise HTTPException(status_code=404, detail="Incorrect Username")
    else:
        is_password = verify_password(formdata.password)
        if not is_password:
            raise HTTPException(status_code=404, detail="Incorrect Password")
        else:
            expires_in = datetime.now(timezone.utc) + timedelta(days=1)
            access_token = create_acces_token(sub={"username":formdata.username , "k_id" :ADMIN_KONG_ID , "exp":expires_in})
            refresh_token = create_refresh_token(sub={"username":formdata.username})
            return Token(access_token=access_token, refresh_token=refresh_token, expires_in=expires_in)