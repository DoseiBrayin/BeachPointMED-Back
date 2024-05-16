from sqlalchemy import Column, String, Float, Int
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
    __tablename__ = 'Products'

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Int)
    active = Column(String)

    def __init__(self, id, name, price, active):
        self.id = id
        self.name = name
        self.price = price
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "active": self.active
        }