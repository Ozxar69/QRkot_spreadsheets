from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


class CRUDCharityProject(CRUDBase):
    """CRUD-операции с благотворительными проектами."""

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Получить id проекта по его названию."""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name,
            )
        )
        return db_project_id.scalars().first()

    async def get_charity_project_by_id(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Получить проект по id."""
        db_project = await session.execute(
            select(CharityProject).where(CharityProject.id == project_id)
        )
        return db_project.scalars().first()

    async def update_charity_project(
        self,
        db_project: CharityProject,
        project_in: CharityProjectUpdate,
        session: AsyncSession,
    ) -> CharityProject:
        """Обновить проект."""
        obj_data = jsonable_encoder(db_project)
        update_data = project_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_project, field, update_data[field])
        session.add(db_project)
        await session.commit()
        await session.refresh(db_project)
        return db_project

    async def delete_charity_project(
        self,
        db_project: CharityProject,
        session: AsyncSession,
    ) -> CharityProject:
        """Удалить из БД проект."""
        await session.delete(db_project)
        await session.commit()
        return db_project


charity_project_crud = CRUDCharityProject(CharityProject)
