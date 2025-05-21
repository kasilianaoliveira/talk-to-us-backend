from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.product_schema import ProductCreateDTO, ProductResponseDTO
from src.services.product_service import ProductService, get_product_service

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post(
    "/",
    status_code=HTTPStatus.CREATED,
    response_model=ProductResponseDTO,
)
async def create_new_user(
    product_data: ProductCreateDTO,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.create_product(product_data)
