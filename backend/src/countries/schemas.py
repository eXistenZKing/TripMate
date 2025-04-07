from pydantic import BaseModel, Field
from typing import Optional


class AttractionBase(BaseModel):
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    category: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    image_url: Optional[str] = None


class AttractionCreate(AttractionBase):
    country_id: int
    city_id: int


class Attraction(AttractionBase):
    id: int
    country_id: int
    city_id: int

    class Config:
        from_attributes = True


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
