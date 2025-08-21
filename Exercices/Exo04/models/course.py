from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from Models.Base import Base


class Course(Base):
    __tablename__ = 'courses'

    id = Column(String(20), primary_key=True)
    name = Column(String(200), nullable=False)
    credits = Column(Integer)
    professor_id = Column(Integer, ForeignKey('professors.id'))

    professor = relationship("Professor", back_populates="courses")
    students = relationship("Student", back_populates="course")