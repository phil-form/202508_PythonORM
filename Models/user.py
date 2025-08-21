from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from Models.Base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column()
    basket_items = relationship('BasketItem', back_populates='user', cascade='all, delete-orphan')
    roles = relationship('Role', back_populates='users', secondary='user_roles')
