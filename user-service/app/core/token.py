from jose import jwt
from app.settings import SECRET_KEY , ALGORITHM
from datetime import datetime, timedelta ,timezone

def create_acces_token(sub:dict):
    encode_token = jwt.encode(sub  , key=SECRET_KEY , algorithm=ALGORITHM)
    return encode_token


def create_refresh_token(sub:dict):
    to_encode = sub.copy()
    expire_in = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": int(expire_in.timestamp())})
    encode_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encode_token


def decode_token(token:str):
    decode_token = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
    return decode_token