from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import database
from src.auth.dependencies import get_current_admin
from src.models import User
from src.cities import crud, schemas
from src.attractions import crud as attractions_crud
from src.attractions import schemas as attractions_schemas

router = APIRouter(prefix="/cities", tags=["Cities"])


@router.get("/{city_id}", response_model=schemas.City)
async def read_city(
    city_id: int,
    db: AsyncSession = Depends(database.async_session)
):
    db_city = await crud.get_city(db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@router.post("/{city_id}/attractions/",
             response_model=attractions_schemas.Attraction)
async def create_attraction(
    city_id: int,
    attraction: attractions_schemas.AttractionCreate,
    db: AsyncSession = Depends(database.async_session),
    current_admin: User = Depends(get_current_admin),
):
    return await attractions_crud.create_attraction(
        db=db, attraction=attraction
    )
