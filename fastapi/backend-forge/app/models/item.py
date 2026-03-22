"""
Database models defining the structure of our tables.
"""
from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class ItemDB(Base):
    """
    SQLAlchemy model for the 'items' table.
    This class represents how items are stored in the database.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_available = Column(Boolean, default=True)
