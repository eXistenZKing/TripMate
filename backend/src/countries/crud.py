from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models import Country, City, Attraction
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
