from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from Models.Base import Base


class BasketItem(Base):
    __tablename__ = 'basketitems'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)

    item_id = Column(Integer, ForeignKey('items.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='basket_items')
    item = relationship('Item', back_populates='basket_items')