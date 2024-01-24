from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.core.config import Settings
from app.models import CharityProject
from constants import (
    CLOSED_PROJECT_EXCEPTION,
    DELETE_PROJECT_EXCEPTION,
    FULL_AMOUNT_EXCEPTION,
    NAME_DUPLICATE_EXCEPTION,
    NOT_INVESTED_YET,
    PROJECT_NOT_EXISTS_EXCEPTION,
)


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession,
) -> None:
    """Проверить уникальность полученного названия проекта."""
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name,
        session,
    )
    if project_id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=NAME_DUPLICATE_EXCEPTION,
        )


async def check_charity_project_exists(
    charity_project_id: int,
    session: AsyncSession,
) -> CharityProject:
    """Проверить, существует ли проект по id."""
    charity_project = await charity_project_crud.get_charity_project_by_id(
        charity_project_id,
        session,
    )
    if charity_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROJECT_NOT_EXISTS_EXCEPTION,
        )
    return charity_project


async def check_before_update(
    charity_project: CharityProject,
):
    """Проверить, можно ли изменять переданный проект."""
    if charity_project.fully_invested is True:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=CLOSED_PROJECT_EXCEPTION,
        )


async def check_full_amount_before_update(
    old_invested_amount: int,
    new_full_amount: int,
):
    """Проверить, можно ли изменять стоимость переданного проекта."""
    if new_full_amount < old_invested_amount:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=FULL_AMOUNT_EXCEPTION,
        )


async def check_before_delete_project(
    charity_project: CharityProject,
):
    """Проверить, можно ли удалять переданный проект."""
    if charity_project.invested_amount != NOT_INVESTED_YET:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=DELETE_PROJECT_EXCEPTION,
        )

async def check_google_api_variables(settings: Settings):
    """Проверяет, что настроечные параметры Google API установлены."""
    if not all([settings.type,
                settings.project_id,
                settings.private_key_id,
                settings.private_key,
                settings.client_email,
                settings.client_id,
                settings.auth_uri,
                settings.token_uri,
                settings.auth_provider_x509_cert_url,
                settings.client_x509_cert_url,
                settings.email]):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=('Невозможно сформировать отчет. '
                    'Ошибка в конфигурационных параметрах. '
                    'Проверьте настройки Google API.')
        )