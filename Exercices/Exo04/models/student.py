from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from Models.Base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    lastname = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"))
    course_id = Column(String(20), ForeignKey("courses.id"), nullable=True)
    year_result = Column(Integer, nullable=True)

    section = relationship("Section", back_populates="students")
    course = relationship("Course", back_populates="students")