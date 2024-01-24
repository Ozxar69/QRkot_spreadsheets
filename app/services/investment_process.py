from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def donation_amount(
    donation: Donation,
    project: CharityProject,
):
    """Определить величину пожертвования."""
    return min(
        project.full_amount - project.invested_amount,
        donation.full_amount - donation.invested_amount,
    )


async def is_fully_invested(value):
    """Определить, инвестированы ли все средства."""
    if value.full_amount == value.invested_amount:
        value.fully_invested = True
        value.close_date = datetime.now()


async def investition(
    main_value: CharityProject,
    values: list[Donation],
    session: AsyncSession,
):
    """Инвестировать пожертвование в проект."""
    for value in values:
        donation_value = await donation_amount(
            donation=value,
            project=main_value,
        )
        value.invested_amount += donation_value
        main_value.invested_amount += donation_value

        await is_fully_invested(value)
        await is_fully_invested(main_value)

    await session.commit()
    await session.refresh(main_value)
