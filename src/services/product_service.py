import uuid
from http import HTTPStatus
from typing import List, Optional

from fastapi import Depends, HTTPException

from src.models.product_model import Product
from src.repositories.product_repository import (
    ProductRepository,
    get_product_repository,
)
from src.repositories.user_repository import (
    UserRepository,
    get_user_repository,
)
from src.schemas.product_schema import ProductInput, ProductOutput


class ProductService:
    def __init__(
        self, product_repository: ProductRepository, user_repository: UserRepository
    ):
        self.product_repository = product_repository
        self.user_repository = user_repository

    async def create_product(self, product_data: ProductInput) -> Product:
        db_user = await self.user_repository.get_user(product_data.user_id)

        existing_product = await self.product_repository.get_product_by_name(
            product_data.name
        )

        if existing_product:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="A product with this name already exists.",
            )

        if not db_user:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="User not found.",
            )

        db_product = Product(**product_data.model_dump())
        created_product = await self.product_repository.create(db_product)

        return created_product

    async def get_all_products_by_user_paginated(
        self,
        user_id: uuid.UUID,
        page: int = 1,
        limit: int = 10,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[ProductOutput]:
        offset = (page - 1) * limit
        products_result = await self.product_repository.get_all_by_user_paginated(
            offset, limit, user_id, name, status
        )

        return [ProductOutput.model_validate(product) for product in products_result]

    async def count_all_products_by_user(
        self,
        user_id: uuid.UUID,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> int:
        return await self.product_repository.count_all_by_user(
            user_id=user_id, name=name, status=status
        )


async def get_product_service(
    product_repository: ProductRepository = Depends(get_product_repository),
    user_repository: UserRepository = Depends(get_user_repository),
):
    return ProductService(product_repository, user_repository)
