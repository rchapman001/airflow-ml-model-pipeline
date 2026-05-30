from fastapi import APIRouter
from app.api.endpoints import company, health

api_router = APIRouter()

api_router.include_router(company.router, tags=["Company"])
api_router.include_router(health.router, tags=["Health"])
