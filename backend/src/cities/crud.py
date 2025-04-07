from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models import City
from . import schemas


async def create_city(db: AsyncSession, city: schemas.CityCreate) -> City:
    db_city = City(**city.model_dump())
    db.add(db_city)
    await db.commit()
    await db.refresh(db_city)
    return db_city


async def get_city(db: AsyncSession, city_id: int) -> City:
    result = await db.execute(
        select(City)
        .options(selectinload(City.attractions))
        .filter(City.id == city_id)
    )
    return result.scalar_one_or_none()


async def get_cities(
    db: AsyncSession, country_id: int, skip: int = 0, limit: int = 100
) -> list[City]:
    result = await db.execute(
        select(City)
        .options(selectinload(City.attractions))
        .filter(City.country_id == country_id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()
