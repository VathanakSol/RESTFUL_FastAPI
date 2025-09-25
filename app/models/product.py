from sqlalchemy import Column, String, Integer, Float, Boolean
from db.session import Base

class Product(Base):
    __tablename__ = "products"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True, nullable=False)
    description=Column(String, unique=True, index=True, nullable=True)
    price=Column(Float, nullable=False)
    stock=Column(Boolean, nullable=False)