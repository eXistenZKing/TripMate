from fastapi import FastAPI

from .auth import router


app = FastAPI(
    title="TripMate"
)

app.include_router(router)
