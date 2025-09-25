from pydantic import BaseModel, EmailStr
from typing import TypeVar, Optional, Generic

T = TypeVar("T")

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config: 
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None

class BaseResponse(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None