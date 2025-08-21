from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.Base import Base


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    titre = Column(String(200))
    annee = Column(Integer)

    acteurs = relationship("Acteur", back_populates="films", secondary="film_acteurs")
    users = relationship("User", back_populates="films", secondary="playlists")
