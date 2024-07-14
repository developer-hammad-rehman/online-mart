from datetime import datetime
import uuid
from sqlmodel import SQLModel , Field


class Users(SQLModel , table=True):
    id : int | None = Field(default=None , primary_key=True)
    username : str
    password : str
    k_id :str = uuid.uuid4().hex



class Token(SQLModel):
    access_token: str
    token_type:str = Field(default="bearer")
    expires_in: datetime
    refresh_token: str


class GPToken(SQLModel):
    access_token: str
    token_type:str = Field(default="bearer")
    expires_in: int
    refresh_token: str



class UpdateUser(SQLModel):
    username: str
    password: str
    new_username:str



class UpdatePassword(SQLModel):
    username: str
    new_password:str