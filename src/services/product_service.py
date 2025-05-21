from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, HTTPException

from src.models.product_model import Product
from src.repositories.product_repository import (
    ProductRepository,
    get_product_repository,
)
from src.schemas.product_schema import ProductCreateDTO


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def create_product(self, product_data: ProductCreateDTO) -> Product:
        existing_product = await self.product_repository.get_product_by_name(
            product_data.name,
        )

        if existing_product:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Product already exists.",
            )

        product = Product(**product_data.model_dump())
        result_product = await self.product_repository.create(product)
        return result_product


async def get_product_service(
    product_repository: Annotated[
        ProductRepository, Depends(get_product_repository)
    ],
):
    return ProductService(product_repository)
