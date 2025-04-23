from http import HTTPStatus
from math import ceil
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query

from src.schemas.product_schema import (
    PaginatedProductResponse,
    ProductInput,
    ProductOutput,
)
from src.services.product_service import ProductService, get_product_service

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post(
    "/create", response_model=ProductOutput, status_code=HTTPStatus.CREATED
)
async def create_new_product(
    product_in: ProductInput,
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.create_product(product_in)


@product_router.get("/", response_model=PaginatedProductResponse)
async def list_products(
    product_service: ProductService = Depends(get_product_service),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    name: Optional[str] = Query(
        None, description="Filter by product name (case-insensitive)"
    ),
    status: Optional[str] = Query(
        None, description="Filter by product status (in_stock or sold_out)"
    ),
    user_id: UUID = Query(None, description="User id"),
):
    # Lógica de validação/filtragem por usuário (se necessário)
    products = await product_service.get_all_products_by_user_paginated(
        page=page,
        limit=limit,
        name=name,
        status=status,
        user_id=user_id,
    )
    total_products = await product_service.count_all_products_by_user(
        name=name, status=status, user_id=user_id
    )
    total_pages = ceil(total_products / limit)
    has_next = page < total_pages
    has_prev = page > 1

    return {
        "items": products,
        "total": total_products,
        "page": page,
        "limit": limit,
        "pages": total_pages,
        "has_next": has_next,
        "has_prev": has_prev,
    }
