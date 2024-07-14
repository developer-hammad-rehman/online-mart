from app.db import get_session
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session


DBSESSION = Annotated[Session , Depends(get_session)]