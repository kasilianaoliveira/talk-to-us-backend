import uuid
from typing import Optional

from sqlmodel import select

from src.db.connection import SessionDep
from src.models.product_model import Product


class ProductRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    async def get_product(self, product_id: uuid.UUID) -> Optional[Product]:
        get_product = await self.session.get(Product, product_id)
        return get_product

    async def get_product_by_name(
        self, product_name: str
    ) -> Optional[Product]:
        result = await self.session.execute(
            select(Product).where(Product.name == product_name)
        )
        return result.scalar_one_or_none()

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)

        return product


async def get_product_repository(session: SessionDep):
    return ProductRepository(session)
