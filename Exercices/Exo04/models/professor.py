from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from Models.Base import Base


class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)
    lastname = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"))
    office =Column(Integer)
    login = Column(String(100), unique=True)
    hire_date = Column(Date)
    salary = Column(Integer)

    section = relationship("Section", back_populates="professors")
    courses = relationship("Course", back_populates="professor")