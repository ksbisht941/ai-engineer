"""
SQLAlchemy database models (database schema).
"""
from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class ItemDB(Base):
    """
    Database model for an Item.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_available = Column(Boolean, default=True)