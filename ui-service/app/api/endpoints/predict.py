from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from app.utils.utils import templates
from app.services.prediction_service import predict

router = APIRouter()


@router.get("/predict", response_class=HTMLResponse)
def predict_page(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})


@router.post("/predict", response_class=HTMLResponse)
def run_prediction(request: Request, text: str = Form(...), model_size: str = Form(...)):
    try:
        result = predict(text, model_size)
        message = "Prediction completed"
    except Exception as e:
        result = None
        message = f"Prediction failed: {str(e)}"

    return templates.TemplateResponse(
        "predict.html",
        {
            "request": request,
            "result": result,
            "message": message,
            "form": {
                "text": text,
                "model_size": model_size,
            },
        },
    )
