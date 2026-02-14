from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.services.airflow_service import trigger_dag
from app.utils.utils import templates

router = APIRouter()


@router.get("/service-health", response_class=HTMLResponse)
def health_page(request: Request):
    return templates.TemplateResponse("service_health.html", {"request": request})


@router.post("/service-health", response_class=HTMLResponse)
def run_service_health(request: Request):
    try:
        result = trigger_dag("service_health_check")
        message = "Service health check DAG triggered successfully"
    except Exception as e:
        result = None
        message = f"Service health check failed: {str(e)}"

    return templates.TemplateResponse(
        "service_health.html",
        {
            "request": request,
            "result": result,
            "message": message,
            "form": {},
        },
    )
