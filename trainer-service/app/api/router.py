from fastapi import APIRouter
from app.api.endpoints import train, health

api_router = APIRouter()

api_router.include_router(train.router, tags=["Train"])
api_router.include_router(health.router, tags=["Health"])
