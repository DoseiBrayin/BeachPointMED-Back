from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from courts.models.courts_model import Courts

Base = declarative_base()

class Timecourts(Base):
    __tablename__ = 'Timecourts'

    id = Column(String(36), primary_key=True)
    fk_court = Column(String(36), ForeignKey(Courts.id),nullable=False)  # Nota el cambio aquí
    date = Column(DateTime)
    hour = Column(Integer)
    price = Column(Float)
    state = Column(String(100))

    court = relationship(Courts, backref='timecourts')
    
    def to_dict(self):
        return {
            "id": self.id,
            "fk_court": self.fk_court,
            "court": self.court.to_dict(),
            "day": self.day,
            "month": self.month,
            "year": self.year,
            "hour": self.hour,
            "price": self.price,
            "state": self.state
        }
