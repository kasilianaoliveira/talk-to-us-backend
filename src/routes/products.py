from http import HTTPStatus
from math import ceil
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from src.schemas.product_schema import (
    PaginatedProductResponse,
    ProductFilterParams,
    ProductInput,
    ProductOutput,
)
from src.services.product_service import ProductService, get_product_service

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post("/", response_model=ProductOutput, status_code=HTTPStatus.CREATED)
async def create_new_product(
    product_in: ProductInput,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.create_product(product_in)


@product_router.get("/", response_model=PaginatedProductResponse)
async def list_products(
    product_service: ProductService = Depends(get_product_service),
    params: ProductFilterParams = Depends(),
    user_id: UUID = Query(None, description="User id"),
):
    products = await product_service.get_all_products_by_user_paginated(
        page=params.page,
        size=params.size,
        name=params.name,
        status=params.status,
        user_id=user_id,
    )
    total_products = await product_service.count_all_products_by_user(
        name=params.name, status=params.status, user_id=user_id
    )
    total_pages = ceil(total_products / params.size)
    # has_next = page < total_pages
    # has_prev = page > 1

    return {
        "items": products,
        "total": total_products,
        "page": params.page,
        "size": params.size,
        "pages": total_pages,
    }
