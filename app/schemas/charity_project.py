from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator

from constants import (
    CREATE_DATE,
    FULL_AMOUNT_GT,
    INVESTED_AMOUNT_DEFAULT,
    PR_DESC_MIN_LEN,
    PR_NAME_MAX_LEN,
    PR_NAME_MIN_LEN,
)


class CharityProjectBase(BaseModel):
    """Базовая схема благотворительного проекта."""

    name: Optional[str] = Field(
        None,
        min_length=PR_NAME_MIN_LEN,
        max_length=PR_NAME_MAX_LEN,
    )
    description: Optional[str] = Field(None, min_length=PR_DESC_MIN_LEN)
    full_amount: Optional[int] = Field(None, gt=FULL_AMOUNT_GT)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    """Схема для создания благотворительного проекта."""

    name: str = Field(
        ...,
        min_length=PR_NAME_MIN_LEN,
        max_length=PR_NAME_MAX_LEN,
    )
    description: str = Field(..., min_length=PR_DESC_MIN_LEN)
    full_amount: int = Field(..., gt=FULL_AMOUNT_GT)


class CharityProjectUpdate(CharityProjectBase):
    """Схема для обновления полей проекта."""

    @validator("name", "description", "full_amount")
    def field_cannot_be_null(cls, value, field):
        if value is None:
            raise ValueError(f"Поле {field.name} не может быть пустым!")
        return value


class CharityProjectDB(CharityProjectCreate):
    """Схема благотворительного проекта в БД."""

    id: int
    invested_amount: int = INVESTED_AMOUNT_DEFAULT
    fully_invested: bool
    create_date: datetime = Field(..., example=CREATE_DATE)
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
