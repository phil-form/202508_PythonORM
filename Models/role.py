from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.Base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    users = relationship('User', back_populates='roles', secondary='user_roles')