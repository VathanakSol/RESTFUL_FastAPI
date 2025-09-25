from pydantic import BaseModel, EmailStr
from typing import TypeVar, Optional, Generic

T = TypeVar("T")

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config: 
        orm_mode = True

class BaseResponse(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None