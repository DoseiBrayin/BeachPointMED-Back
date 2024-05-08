from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from rol.model.rol_model import Rol

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(String(36), primary_key=True, index=True)
    cedula = Column(String(20), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    password = Column(String(100), nullable=False)
    card_id = Column(String(20))
    is_employee = Column(Boolean, nullable=False)
    fk_rol = Column(String(36), ForeignKey(Rol.id), nullable=False)

    rol = relationship(Rol, backref='users')