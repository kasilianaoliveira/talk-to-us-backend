import uuid
from typing import List, Optional
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.infra.core.connection import SessionDep
from src.models.product_model import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_product_by_name(self, name: str) -> Optional[Product]:
        result = await self.session.execute(
            select(Product).where(func.lower(Product.name) == func.lower(name))
        )
        return result.scalar_one_or_none()

    async def get(self, product_id: UUID, user_id: UUID) -> Optional[Product]:
        return await self.session.get(Product, {"id": product_id, "user_id": user_id})

    async def get_all_by_user_paginated(
        self,
        offset: int,
        limit: int,
        user_id: UUID,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[Product]:
        query = select(Product).where(Product.user_id == user_id)

        if name:
            query = query.where(
                func.lower(Product.name).like(f"%{name.lower()}%"),
            )

        if status:
            query = query.where(Product.status == status)

        result = await self.session.execute(
            query.offset(offset).limit(limit),
        )
        return list(result.scalars().all())

    async def count_all_by_user(
        self,
        user_id: uuid.UUID,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> int:
        query = select(Product).where(Product.user_id == user_id)
        if name:
            query = query.where(func.lower(Product.name).like(f"%{name.lower()}%"))
        if status:
            # Filtra diretamente pela string do status
            query = query.where(Product.status == status)
        result = await self.session.execute(query)
        return len(result.scalars().all())

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)

        return product


async def get_product_repository(session: SessionDep):
    return ProductRepository(session)
