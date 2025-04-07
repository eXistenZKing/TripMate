from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models import Country
from . import schemas


async def create_country(db: AsyncSession, country: schemas.CountryCreate
                         ) -> Country:
    db_country = Country(**country.model_dump())
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country


async def get_country(db: AsyncSession, country_id: int) -> Country:
    result = await db.execute(
        select(Country)
        .options(
            selectinload(Country.cities), selectinload(Country.attractions)
        )
        .filter(Country.id == country_id)
    )
    return result.scalar_one_or_none()


async def get_countries(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> list[Country]:
    result = await db.execute(
        select(Country)
        .options(
            selectinload(Country.cities), selectinload(Country.attractions)
        )
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()
