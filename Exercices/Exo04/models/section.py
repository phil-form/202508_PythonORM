from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Models.Base import Base


class Section(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    nb_students = Column(Integer, nullable=False)
    delegate_id = Column(Integer)

    professors = relationship("Professor", back_populates="section")
    students = relationship("Student", back_populates="section")