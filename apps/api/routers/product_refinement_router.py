from fastapi import APIRouter

from apps.api.schemas.product_refinement_schemas import (
    ProductRefinementRequest,
    ProductRefinementResponse,
)
from apps.api.services.product_refinement_mock_service import (
    generate_mock_product_refinement,
)

router = APIRouter(prefix="/product-refinement", tags=["Product Refinement"])


@router.post("/generate", response_model=ProductRefinementResponse)
def generate_product_refinement(
    request: ProductRefinementRequest,
) -> ProductRefinementResponse:
    return generate_mock_product_refinement(request)