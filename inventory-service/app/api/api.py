from fastapi import APIRouter
from app.api.routes import enpoints

router = APIRouter()


router.include_router(enpoints.endpoint_router)