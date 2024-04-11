from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Location(Base):
    __tablename__ = 'Location'

    id = Column(String(36), primary_key=True)
    description = Column(String(200))
    address = Column(String(100))
    active = Column(Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "address": self.address,
            "active": self.active
        }