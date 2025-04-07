from typing import Optional

from pydantic import BaseModel

from src.attractions.schemas import Attraction
from src.cities.schemas import City


class CountryBase(BaseModel):
    name: str
    description: Optional[str] = None
    capital: Optional[str] = None
    population: Optional[int] = None
    area: Optional[int] = None
    currency: Optional[str] = None
    language: Optional[str] = None
    flag_url: Optional[str] = None


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int
    cities: list[City] = []
    attractions: list[Attraction] = []

    class Config:
        from_attributes = True
