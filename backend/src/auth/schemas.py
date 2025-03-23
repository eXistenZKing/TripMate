from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserIn(UserBase):
    email: EmailStr
    password: str


class UserOut(UserBase):
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
