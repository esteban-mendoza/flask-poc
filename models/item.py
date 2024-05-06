import uuid

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    price = Column(Float(precision=2), nullable=False)
    store_id = Column(
        Integer, ForeignKey("stores.store_id"), unique=False, nullable=False
    )

    store = db.relationship("StoreModel", back_populates="items")
