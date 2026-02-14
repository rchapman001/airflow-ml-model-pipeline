from fastapi import APIRouter
from app.api.endpoints import health, predict, train, service_health

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(predict.router, tags=["Predict"])
api_router.include_router(train.router, tags=["Train"])
api_router.include_router(service_health.router, tags=["Service Health"])
