from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    email_confirmed: Mapped[bool] = mapped_column(
        Boolean, server_default="false", nullable=False
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("roles.id"), default=1
    )

    role: Mapped["Role"] = relationship(back_populates="users")


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    users: Mapped[list["User"]] = relationship(back_populates="role")
