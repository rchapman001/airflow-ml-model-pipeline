from fastapi import FastAPI
from app.api.router import api_router
from app.config.constants import SERVICE_PREFIX

app = FastAPI(title="Scraper Service")

app.include_router(api_router, prefix=f"{SERVICE_PREFIX}")
