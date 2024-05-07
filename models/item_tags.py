from sqlalchemy import Column, ForeignKey, Integer

from db import db


class ItemsTags(db.Model):

    __tablename__ = "items_tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
