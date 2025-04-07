from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import database
from src.attractions import crud, schemas

router = APIRouter(prefix="/attractions", tags=["Attractions"])


@router.get("/", response_model=List[schemas.Attraction])
async def read_attractions(
    country_id: int | None = None,
    city_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(database.async_session),
):
    attractions = await crud.get_attractions(
        db,
        country_id=country_id,
        city_id=city_id,
        skip=skip,
        limit=limit,
    )
    return attractions


@router.get("/{attraction_id}", response_model=schemas.Attraction)
async def read_attraction(
    attraction_id: int, db: AsyncSession = Depends(database.async_session)
):
    db_attraction = await crud.get_attraction(db, attraction_id=attraction_id)
    if db_attraction is None:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return db_attraction
