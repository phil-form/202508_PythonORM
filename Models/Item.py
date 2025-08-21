from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from Models.Base import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)

    basket_items = relationship('BasketItem', back_populates='item')