from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.settings import USER_SERVICE_URL 


oauth_scheme = OAuth2PasswordBearer(tokenUrl=f"{USER_SERVICE_URL}/login")


TOKEN_DEPS = Annotated[str , Depends(oauth_scheme)]