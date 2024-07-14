from fastapi  import APIRouter
from app.api.routes import login
from app.api.routes import signup
from app.api.routes import health
from app.api.routes import admin
from app.api.routes import auth_crud

router  = APIRouter()

router.include_router(health.heath_router)
router.include_router(login.login_router)
router.include_router(signup.signup_router)
router.include_router(admin.admin_router)
router.include_router(auth_crud.auth_crud)