from sqlalchemy import Column, Integer, String

from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)

    items = db.relationship(
        "ItemModel",
        back_populates="store",
        lazy="dynamic",
        cascade="all, delete",
    )
