from fastapi import APIRouter

heath_router = APIRouter(tags=["Health Routes"])

@heath_router.get("/health")
def health():
    return {"status" : "ok"}

@heath_router.get("/version")
def version():
    return {"version" : "1.0.0"}

@heath_router.get("/info")
def info():
    return {"app_name" : "User Service" , "app_version" : "1.0.0"}