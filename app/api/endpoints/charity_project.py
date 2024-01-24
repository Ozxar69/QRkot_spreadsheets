from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_before_delete_project,
    check_before_update,
    check_charity_project_exists,
    check_full_amount_before_update,
    check_name_duplicate,
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)
from app.services.investment_process import investition

router = APIRouter()


@router.post(
    "/",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def create_new_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать новый проект (Только для суперюзеров)."""
    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    donations = await donation_crud.free_objects(session)
    await investition(
        main_value=new_project,
        values=donations,
        session=session,
    )
    return new_project


@router.patch(
    "/{charity_project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_project(
    charity_project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Редактировать существующий проект (Только для суперюзеров)."""
    charity_project = await check_charity_project_exists(
        charity_project_id,
        session,
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)

    await check_before_update(charity_project)

    if obj_in.full_amount is not None:
        await check_full_amount_before_update(
            charity_project.invested_amount,
            obj_in.full_amount,
        )

    return await charity_project_crud.update_charity_project(
        charity_project,
        obj_in,
        session,
    )


@router.delete(
    "/{charity_project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Удалить проект (Только для суперюзеров)."""
    charity_project = await check_charity_project_exists(
        charity_project_id,
        session,
    )
    await check_before_delete_project(charity_project)

    return await charity_project_crud.delete_charity_project(
        charity_project,
        session,
    )


@router.get(
    "/",
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
) -> list[CharityProjectDB]:
    """Получить список всех проектов."""
    return await charity_project_crud.get_multi(session)
