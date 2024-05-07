from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=False, nullable=False)
    store_id = Column(Integer, db.ForeignKey("stores.id"), nullable=False)

    store = relationship("StoreModel", back_populates="tags")
    items = relationship("ItemModel", back_populates="tags", secondary="items_tags")
