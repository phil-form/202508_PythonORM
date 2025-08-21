from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.Base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    films = relationship('Film', back_populates='users', secondary='playlists')