from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class CRUDBase:
    """Получает все объекты класса или создать новые."""

    def __init__(self, model):
        self.model = model

    async def get_multi(
        self,
        session: AsyncSession,
    ):
        """Получает все объекты заданного класса."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
        user: Optional[User] = None,
    ):
        """Создает новый объект."""
        obj_in_data = obj_in.dict()

        if user is not None:
            obj_in_data["user_id"] = user.id

        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def free_objects(
        self,
        session: AsyncSession,
    ):
        """Проверка существования объектов для инвестирования."""
        objects = await session.execute(
            select(self.model)
            .where(
                self.model.fully_invested == 0,
            )
            .order_by(self.model.create_date)
        )
        return objects.scalars().all()
