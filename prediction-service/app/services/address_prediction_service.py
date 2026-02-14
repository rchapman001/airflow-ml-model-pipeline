from app.utils.utils import get_nlp
from app.models.prediction_models import PredictionResponse


async def predict_address(text: str, model_path: str) -> PredictionResponse:
    nlp = get_nlp(model_path)
    doc = nlp(text)

    entities = {ent.label_: ent.text for ent in doc.ents}

    return PredictionResponse(text=text, entities=entities)
