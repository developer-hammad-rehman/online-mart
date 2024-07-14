from pydantic import BaseModel


class CustomNotification(BaseModel):
    message: str
    username: str