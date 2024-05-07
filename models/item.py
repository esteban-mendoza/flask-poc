from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    price = Column(Float(precision=2), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), unique=False, nullable=False)

    store = relationship("StoreModel", back_populates="items")
    tags = relationship("TagModel", back_populates="items", secondary="items_tags")
