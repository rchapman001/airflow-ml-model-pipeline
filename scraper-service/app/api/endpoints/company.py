from fastapi import APIRouter, Query

from app.config.constants import DATASET_PATHS
from app.models.scrape_models import ScrapeResponse
from app.models.input_size import InputSize
from app.services.company_service import get_company_addresses

router = APIRouter()


@router.get(
    "/company-address",
    response_model=ScrapeResponse,
)
async def company_address(
    size: InputSize = Query(
        default=InputSize.small,
        description="Size of input dataset: small, medium, or large",
    ),
):
    paths = DATASET_PATHS[size.value]

    return await get_company_addresses(
        input_path=paths["input"],
        output_path=paths["output"],
    )
