from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)

    items = relationship(
        "ItemModel",
        back_populates="store",
        lazy="dynamic",
        cascade="all, delete",
    )
    tags = relationship(
        "TagModel",
        back_populates="store",
        lazy="dynamic",
        cascade="all, delete",
    )
