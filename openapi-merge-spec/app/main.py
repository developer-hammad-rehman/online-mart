from fastapi import FastAPI
import requests

app = FastAPI(
    title="User Openapi Merge Spec",
    version="1.0.0",
    servers=[
        {
            "url":"http://localhost:8000",
            "description":"local server"
        }
    ]
)


@app.get('/')
async def root():
    return {"message": "User Openapi Merge Spec"}



