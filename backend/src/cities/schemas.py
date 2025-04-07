from typing import Optional

from pydantic import BaseModel

from src.attractions.schemas import Attraction


class CityBase(BaseModel):
    name: str
    description: Optional[str] = None
    population: Optional[int] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None


class CityCreate(CityBase):
    country_id: int


class City(CityBase):
    id: int
    country_id: int
    attractions: list[Attraction] = []

    class Config:
        from_attributes = True
