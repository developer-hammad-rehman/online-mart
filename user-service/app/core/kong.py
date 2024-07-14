# from fastapi import HTTPException
# import requests  # type: ignore
# from app.settings import KONG_ADMIN_URL, SECRET_KEY


# def create_consumer_in_kong(user_name: str):
#     print("Creating consumer in Kong")
#     response = requests.post(f"{KONG_ADMIN_URL}/consumers", data={"username": user_name})
#     print(response.json())


# def create_jwt_credential_in_kong(user_name: str, k_id: str):
#     print("Creating JWT credential in Kong")
#     response = requests.post(
#         f"{KONG_ADMIN_URL}/consumers/{user_name}/jwt", data={"key": k_id , "secret" : SECRET_KEY})
#     if response.status_code != 201:
#         raise HTTPException(status_code=500, detail="Error creating JWT credential in Kong")