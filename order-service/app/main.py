from typing import Optional
from fastapi import FastAPI, Form 
from fastapi.responses import RedirectResponse
from app.db import create_table
from contextlib import asynccontextmanager
from app.api.api import router
from app.core.kafka_schema import event_up
import requests

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    await event_up()
    yield

app = FastAPI(
    title="Order Service", 
    lifespan=lifespan, 
     servers=[
        {
            "url": "https://order-service.bluedune-2d8c02d1.eastus.azurecontainerapps.io",
            "description": "Production Url",
        }
    ],
)


@app.get("/" , tags=["Root Route"])
async def root_route():
    return {"message": "Order Service"}



@app.get('/login' , tags=['Login'])
async def login(redirect_uri:str , state:str , client_id:str , response_type:str  , scope:str):
    qurey = f"?redirect_uri={redirect_uri}&state={state}&client_id={client_id}&response_type={response_type}&scope={scope}"
    return RedirectResponse(url=f"https://martnest.vercel.app/login{qurey}")

@app.post("/oauth-token", tags=["Token Url"])
def token_route(grant_type: str = Form(...), refresh_token: Optional[str] = Form(None), code: Optional[str] = Form(None)):
   response = requests.post(
        "https://user-service.bluedune-2d8c02d1.eastus.azurecontainerapps.io/oauth-token",
        data={"grant_type": grant_type, "refresh_token": refresh_token, "code": code},
    )
   return response.json()
app.include_router(router)