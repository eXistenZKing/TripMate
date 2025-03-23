from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from .schemas import UserIn, UserOut, Token
from .crud import (
    create_user,
    get_current_active_user,
    get_user,
    authenticate_user,
    create_access_token
)
from src.core import database, settings


router = APIRouter(
    prefix="/auth",
    tags=["Auth",]
)


@router.post("/register", response_model=UserOut)
async def register_user(
    user_in: UserIn, db: AsyncSession = Depends(database.async_session)
):
    user = await get_user(db, user_in.username)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = await create_user(db, user_in)
    return new_user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(database.async_session)
) -> Token:
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.auth.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me", response_model=UserOut)
async def read_users_me(
    current_user: Annotated[UserOut, Depends(get_current_active_user)]
):
    return current_user
