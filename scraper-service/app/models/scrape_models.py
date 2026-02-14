from pydantic import BaseModel


class ScrapeResponse(BaseModel):
    status: str
    records_written: int
