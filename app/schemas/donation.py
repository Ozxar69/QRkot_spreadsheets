from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from constants import (
    CREATE_DATE,
    DON_COMMENT_MIN_LEN,
    FULL_AMOUNT_GT,
    INVESTED_AMOUNT_DEFAULT,
)


class DonationCreate(BaseModel):
    """Схема для создания пожертвования."""

    full_amount: int = Field(..., gt=FULL_AMOUNT_GT)
    comment: Optional[str] = Field(
        None,
        min_length=DON_COMMENT_MIN_LEN,
    )


class DonationDB(DonationCreate):
    """Схема пожертвования в БД."""

    id: int
    create_date: datetime = Field(..., example=CREATE_DATE)
    user_id: Optional[int]
    invested_amount: int = INVESTED_AMOUNT_DEFAULT
    fully_invested: bool = False
    close_date: Optional[datetime] = None

    class Config:
        orm_mode = True
