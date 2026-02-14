from pydantic import BaseModel


class TrainResponse(BaseModel):
    status: str
    examples_used: int
    model_path: str
