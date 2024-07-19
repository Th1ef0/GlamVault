from sqlalchemy import Column, String, Integer, Float, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class ProductDB(Base):
    __tablename__ = "products"

    id: int = Column("id", Integer, primary_key=True, index=True)
    name: str = Column("name", String, index=True)
    description: str = Column("description", String)
    price: float = Column("price", Float)
    # img: bytes = Column("img", LargeBinary)

    def __init__(self, name: str, description: str, price: float):
        # self.id = id

        self.name = name
        self.description = description
        self.price = price
        # self.img = img

    def __repr__(self):
        return f"({self.id}): {self.name}, {self.price}"
    
class ProductAPI(BaseModel):
    name: str
    description: str
    price: float 