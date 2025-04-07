from typing import Optional

from pydantic import BaseModel, Field


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
