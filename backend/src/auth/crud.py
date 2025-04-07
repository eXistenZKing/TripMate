from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from .schemas import UserIn
from .security import get_password_hash


async def create_user(db: AsyncSession, user_in: UserIn) -> User:
    hashed_password = get_password_hash(user_in.password)
    new_user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
