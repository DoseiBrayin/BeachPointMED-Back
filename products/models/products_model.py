from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
    __tablename__ = 'Products'

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    active = Column(String)

    def __init__(self, id, name, price, active, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.active = active
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "active": self.active,
            "quantity": self.quantity
        }