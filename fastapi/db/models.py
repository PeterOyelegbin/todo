from sqlalchemy import Column, Integer, String, Text, Boolean
from .db_config import Base


# create database model
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    description = Column(Text, nullable=True)
    done = Column(Boolean, default=False)
