from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models import Attraction
from . import schemas


async def create_attraction(
    db: AsyncSession, attraction: schemas.AttractionCreate
) -> Attraction:
    db_attraction = Attraction(**attraction.model_dump())
    db.add(db_attraction)
    await db.commit()
    await db.refresh(db_attraction)
    return db_attraction


async def get_attraction(db: AsyncSession, attraction_id: int) -> Attraction:
    result = await db.execute(
        select(Attraction).filter(Attraction.id == attraction_id)
    )
    return result.scalar_one_or_none()


async def get_attractions(
    db: AsyncSession,
    country_id: int | None = None,
    city_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
) -> list[Attraction]:
    query = select(Attraction)
    if country_id:
        query = query.filter(Attraction.country_id == country_id)
    if city_id:
        query = query.filter(Attraction.city_id == city_id)
    result = await db.execute(query.offset(skip).limit(limit))
    return result.scalars().all()
