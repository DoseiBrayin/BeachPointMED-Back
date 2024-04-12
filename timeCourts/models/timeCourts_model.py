from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Timecourts(Base):
    __tablename__ = 'Timecourts'

    id = Column(String(36), primary_key=True)
    fk_court = Column(String(36), ForeignKey('Courts.id'))  # Nota el cambio aquí
    day = Column(String(12))
    month = Column(String(12))
    year = Column(String(12))
    hour = Column(Integer)
    price = Column(Float)

    # Definir la relación aquí
    def court(self):
        from courts.models import Courts  # Importación local
        return relationship(Courts, back_populates='timecourts')
    
    def to_dict(self):
        return {
            "id": self.id,
            "fk_court": self.fk_court,
            "court": self.court.to_dict(),
            "day": self.day,
            "month": self.month,
            "year": self.year,
            "hour": self.hour,
            "price": self.price
        }
