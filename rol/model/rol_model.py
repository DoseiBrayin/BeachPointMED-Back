from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rol(Base):
    __tablename__ = 'Rol'

    id = Column(String(36), primary_key=True, index=True)
    type_rol = Column(String(100))
