from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.Base import Base


class Acteur(Base):
    __tablename__ = "acteurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String)

    films = relationship("Film", back_populates="acteurs", secondary="film_acteurs")