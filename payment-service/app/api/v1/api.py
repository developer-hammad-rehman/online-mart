from fastapi import APIRouter
from app.api.v1.endpoint import payment_endpoint


router = APIRouter()

router.include_router(payment_endpoint.payment_router ,  prefix="/payment")