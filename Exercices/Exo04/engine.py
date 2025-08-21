from sqlalchemy import create_engine, select, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import Session, DeclarativeBase, declarative_base
from models.Base import Base
from models.section import Section
from models.professor import Professor
from models.course import Course
from models.student import Student
from models.grade import Grade

engine = create_engine(url='sqlite:///myfile.db', echo=True)

# Crée les tables liées à Base
# Il va récupérer toutes les classes qui sont liées à Base
# Et créer les requêtes CREATE TABLE
Base.metadata.create_all(engine)

with Session(engine) as session:

    grade = Grade(grade="A", min=1, max=2)

    session.commit()



