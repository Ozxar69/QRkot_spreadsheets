from sqlalchemy import Column, String, Text

from app.models.custom_base import CustomBase
from constants import PR_NAME_MAX_LEN


class CharityProject(CustomBase):
    """Модель благотворительного проекта."""

    name = Column(String(PR_NAME_MAX_LEN), unique=True, nullable=False)
    description = Column(Text, nullable=False)
