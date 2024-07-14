from fastapi import APIRouter
from app.api.routes import user, admin

router = APIRouter()

router.include_router(user.user_router)
router.include_router(admin.admin_router)