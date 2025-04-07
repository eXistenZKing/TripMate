from fastapi import FastAPI

from src.auth import router as auth_router
from src.api import (
    countries_router,
    cities_router,
    attractions_router
)


app = FastAPI(
    title="TripMate",
    description="API for travel planning and management",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/auth")
app.include_router(countries_router)
app.include_router(cities_router)
app.include_router(attractions_router)
