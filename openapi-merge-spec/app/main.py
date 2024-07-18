from fastapi import FastAPI
from app.routes.product_routes import product_router
from app.routes.order_routes import order_router

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

app.include_router(product_router , tags=["product routes"] , prefix="/api/product-service")

app.include_router(order_router, tags=["order routes"], prefix="/api/order-service")