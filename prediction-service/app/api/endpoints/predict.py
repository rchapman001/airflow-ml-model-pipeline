from fastapi import APIRouter, Query

from app.models.prediction_models import PredictionRequest, PredictionResponse
from app.models.input_size import InputSize
from app.config.constants import MODEL_PATHS
from app.services.address_prediction_service import predict_address

router = APIRouter()


@router.post("/predict-address", response_model=PredictionResponse)
async def predict_address_endpoint(
    request: PredictionRequest,
    size: InputSize = Query(
        default=InputSize.small,
        description="Model size to use: small, medium, or large",
    ),
):
    model_path = MODEL_PATHS[size]

    return await predict_address(request.text, model_path)
