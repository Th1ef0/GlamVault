from pydantic import BaseModel
from sqlalchemy import Float, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class ProductDB(Base):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    description = mapped_column(String)
    price = mapped_column(Float)
    img = mapped_column(String)


class ProductAPI(BaseModel):
    name: str
    description: str
    price: float
    img: str
