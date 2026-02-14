from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app.api.router import api_router
from app.config.settings import get_settings

app = FastAPI(title="UI Service")

app.mount("/static", StaticFiles(directory="app/web/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    from app.utils.utils import templates

    return templates.TemplateResponse("train.html", {"request": request})


app.include_router(api_router, prefix=get_settings().SERVICE_PREFIX)
