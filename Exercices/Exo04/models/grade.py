from sqlalchemy import Column, Integer, String

from Models.Base import Base


class Grade(Base):
    __tablename__ = 'grades'

    grade = Column(String(5), primary_key=True)
    min = Column(Integer)
    max = Column(Integer)