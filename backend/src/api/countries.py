from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import database
from src.auth.dependencies import get_current_admin
from src.models import User
from src.countries import crud, schemas
from src.cities import crud as cities_crud
from src.cities import schemas as cities_schemas

router = APIRouter(prefix="/countries", tags=["Countries"])


@router.post("/", response_model=schemas.Country)
async def create_country(
    country: schemas.CountryCreate,
    db: AsyncSession = Depends(database.async_session),
    current_admin: User = Depends(get_current_admin),
):
    return await crud.create_country(db=db, country=country)


@router.get("/", response_model=List[schemas.Country])
async def read_countries(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(database.async_session)
):
    countries = await crud.get_countries(db, skip=skip, limit=limit)
    return countries


@router.get("/{country_id}", response_model=schemas.Country)
async def read_country(
    country_id: int,
    db: AsyncSession = Depends(database.async_session)
):
    db_country = await crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


@router.post("/{country_id}/cities/", response_model=cities_schemas.City)
async def create_city(
    country_id: int,
    city: cities_schemas.CityCreate,
    db: AsyncSession = Depends(database.async_session),
    current_admin: User = Depends(get_current_admin),
):
    return await cities_crud.create_city(db=db, city=city)


@router.get("/{country_id}/cities/", response_model=List[cities_schemas.City])
async def read_cities(
    country_id: int,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(database.async_session),
):
    cities = await cities_crud.get_cities(
        db, country_id=country_id, skip=skip, limit=limit
    )
    return cities
