from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Courts(Base):
    __tablename__ = 'Courts'

    id = Column(String(36), primary_key=True)
    fk_location = Column(String(36), ForeignKey('Location.id'))  # Aquí usamos una cadena en lugar de la clase Location
    location = relationship('Location')  # Aquí también
    description = Column(String(200))
    state = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "fk_location": self.fk_location,
            "location": self.location.to_dict(),
            "description": self.description,
            "state": self.state
        }
    
    def location(self):
        from courts.models import Location
        return relationship(Location, back_populates='courts')