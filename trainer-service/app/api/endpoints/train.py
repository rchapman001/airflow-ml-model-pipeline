from fastapi import APIRouter, Query

from app.config.constants import DATASET_PATHS, N_ITER
from app.models.train_models import TrainResponse
from app.models.input_size import InputSize
from app.services.train_address_model import train_address_model

router = APIRouter()


@router.get("/train-address-model", response_model=TrainResponse)
def train_address(
    size: InputSize = Query(
        default=InputSize.small,
        description="Size of input dataset: small, medium, or large",
    ),
):
    """
    Train the spaCy address NER model
    """

    paths = DATASET_PATHS[size.value]

    return train_address_model(
        input_path=paths["input"], model_output_path=paths["output"], n_iter=N_ITER
    )
