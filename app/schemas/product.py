from pydantic import BaseModel, Field
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=10)
    description: str | None = None
    price: float = Field(..., gt=1)
    stock: bool 

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=10)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=1)
    stock: Optional[bool] = None

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True

class BaseResponse(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
