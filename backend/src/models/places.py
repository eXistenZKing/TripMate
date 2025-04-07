from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from src.core import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(Text)
    capital = Column(String(100))
    population = Column(Integer)
    area = Column(Integer)
    currency = Column(String(50))
    language = Column(String(100))
    flag_url = Column(String(255))

    cities = relationship("City", back_populates="country")
    attractions = relationship("Attraction", back_populates="country")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    description = Column(Text)
    population = Column(Integer)
    latitude = Column(String(20))
    longitude = Column(String(20))

    country = relationship("Country", back_populates="cities")
    attractions = relationship("Attraction", back_populates="city")


class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    description = Column(Text)
    country_id = Column(Integer, ForeignKey("countries.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))
    address = Column(String(255))
    latitude = Column(String(20))
    longitude = Column(String(20))
    category = Column(String(100))
    rating = Column(Integer)
    image_url = Column(String(255))

    country = relationship("Country", back_populates="attractions")
    city = relationship("City", back_populates="attractions")
