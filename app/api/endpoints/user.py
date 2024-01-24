from fastapi import APIRouter, HTTPException, status

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate
from constants import (
    DELETE_ROUTE,
    DELETE_TAG,
    DELETE_USER_EXCEPTION,
    USER_AUTH_ROUTER_PREFIX,
    USER_AUTH_ROUTER_TAG,
    USER_REGISTER_ROUTER_PREFIX,
    USER_REGISTER_ROUTER_TAG,
    USERS_PREFIX,
    USERS_TAG,
)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=USER_AUTH_ROUTER_PREFIX,
    tags=[USER_AUTH_ROUTER_TAG],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=USER_REGISTER_ROUTER_PREFIX,
    tags=[USER_REGISTER_ROUTER_TAG],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix=USERS_PREFIX,
    tags=[USERS_TAG],
)


@router.delete(
    DELETE_ROUTE,
    tags=[DELETE_TAG],
    deprecated=True,
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail=DELETE_USER_EXCEPTION,
    )
