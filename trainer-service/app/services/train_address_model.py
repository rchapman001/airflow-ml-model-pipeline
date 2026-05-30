import json
import logging
from app.models.train_models import TrainResponse
from app.utils.utils import train_ner_model

logger = logging.getLogger(__name__)


def train_address_model(input_path: str, model_output_path: str, n_iter: int = 20) -> TrainResponse:
    """
    Train the address NER model from spaCy-ready JSON
    with detailed logging for debugging bad records.
    """

    try:
        with open(input_path, "r") as f:
            training_data = json.load(f)
    except Exception:
        print("Failed to load training data")
        return TrainResponse(status="failed", examples_used=0, model_path="")

    if not training_data:
        print("No training data found — aborting training")
        return TrainResponse(status="failed", examples_used=0, model_path="")

    print(f"Loaded %d training examples", len(training_data))

    try:
        train_ner_model(training_data=training_data, output_dir=model_output_path, n_iter=n_iter)

    except Exception:
        print("Address NER training failed")
        return TrainResponse(status="failed", examples_used=0, model_path="")

    print(
        f"Address NER training completed successfully | "
        f"examples_used={len(training_data)} | "
        f"model_path={model_output_path}"
    )

    return TrainResponse(
        status="success", examples_used=len(training_data), model_path=str(model_output_path)
    )
