from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from app.utils.utils import templates
from app.services.airflow_service import trigger_dag

router = APIRouter()


@router.get("/train", response_class=HTMLResponse)
def train_page(request: Request):
    return templates.TemplateResponse("train.html", {"request": request})


@router.post("/train", response_class=HTMLResponse)
def start_training(request: Request, model_size: str = Form(...)):
    try:
        result = trigger_dag(
            dag_id="company_address_parser",
            conf={"size": model_size},
        )
        message = f"Training started for {model_size} model"
    except Exception as e:
        result = None
        message = f"Failed to start training: {str(e)}"

    return templates.TemplateResponse(
        "train.html",
        {
            "request": request,
            "result": result,
            "message": message,
            "form": {
                "model_size": model_size,
            },
        },
    )
