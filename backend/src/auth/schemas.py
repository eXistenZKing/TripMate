from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=6, max_length=50)


class UserIn(UserBase):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=12, max_length=50)


class UserOut(UserBase):
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
