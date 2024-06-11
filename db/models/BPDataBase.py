from sqlalchemy import Column, String, Boolean, Date, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
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

class Courts(Base):
    __tablename__ = 'Courts'
    id = Column(String(36), primary_key=True)
    fk_location = Column(String(36), ForeignKey('Location.id'))
    description = Column(String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "fk_location": self.fk_location,
            "description": self.description
        }

class Timecourts(Base):
    __tablename__ = 'Timecourts'
    id = Column(String(36), primary_key=True)
    fk_court = Column(String(36), ForeignKey('Courts.id'))
    date = Column(Date)
    hour = Column(Integer)
    price = Column(Float)
    state = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "fk_court": self.fk_court,
            "date": self.date,
            "hour": self.hour,
            "price": self.price,
            "state": self.state
        }

class Rol(Base):
    __tablename__ = 'Rol'
    id = Column(String(36), primary_key=True)
    type_rol = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "type_rol": self.type_rol
        }

class Users(Base):
    __tablename__ = 'Users'
    id = Column(String(36), primary_key=True)
    cedula = Column(String(20), unique=True)
    phone_number = Column(String(20))
    email = Column(String(100), unique=True)
    name = Column(String(150))
    password = Column(String(100))
    card_id = Column(String(20))
    is_employee = Column(Boolean)
    fk_rol = Column(String(36), ForeignKey('Rol.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "cedula": self.cedula,
            "phone_number": self.phone_number,
            "email": self.email,
            "name": self.name,
            "password": self.password,
            "card_id": self.card_id,
            "is_employee": self.is_employee,
            "fk_rol": self.fk_rol
        }

class Products(Base):
    __tablename__ = 'Products'
    id = Column(String(36), primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    active = Column(Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "active": self.active
        }

class PromotionalCode(Base):
    __tablename__ = 'PromotionalCode'
    id = Column(String(36), primary_key=True)
    code = Column(String(50))
    porc_discount = Column(Float)
    fk_user = Column(String(36), ForeignKey('Users.id'))
    expiration_date = Column(String(12))

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "porc_discount": self.porc_discount,
            "fk_user": self.fk_user,
            "expiration_date": self.expiration_date
        }

class Reservation(Base):
    __tablename__ = 'Reservation'
    id = Column(String(36), primary_key=True)
    date = Column(Date)
    fk_user = Column(String(36), ForeignKey('Users.id'))
    fk_promotional_code = Column(String(36), ForeignKey('PromotionalCode.id'))
    payed = Column(Boolean)
    ticket_token = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "fk_user": self.fk_user,
            "fk_promotional_code": self.fk_promotional_code,
            "payed": self.payed,
            "ticket_token": self.ticket_token
        }

class ReservationDetails(Base):
    __tablename__ = 'ReservationDetails'
    id = Column(String(36), primary_key=True)
    fk_reservation = Column(String(36), ForeignKey('Reservation.id'))
    fk_product = Column(String(36), ForeignKey('Products.id'))
    total = Column(Float)
    fk_timecourt = Column(String(36), ForeignKey('Timecourts.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "fk_reservation": self.fk_reservation,
            "fk_product": self.fk_product,
            "total": self.total,
            "fk_timecourt": self.fk_timecourt
        }

class ReservationEmployee(Base):
    __tablename__ = 'ReservationEmployee'
    id = Column(String(36), primary_key=True)
    fk_reservation_details = Column(String(36), ForeignKey('ReservationDetails.id'))
    fk_user = Column(String(36), ForeignKey('Users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "fk_reservation_details": self.fk_reservation_details,
            "fk_user": self.fk_user
        }

