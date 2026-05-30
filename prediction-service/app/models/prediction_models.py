from pydantic import BaseModel
from typing import Dict


class PredictionRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    text: str
    entities: Dict[str, str]
