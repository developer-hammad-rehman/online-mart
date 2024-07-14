from fastapi import APIRouter
from app.api.routes import admin
from app.api.routes import user

router = APIRouter()


router.include_router(admin.admin_router)
router.include_router(user.user_router)