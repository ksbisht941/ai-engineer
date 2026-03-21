"""
Pydantic schemas for data validation and response formatting.
"""
from pydantic import BaseModel

class Item(BaseModel):
    """
    Schema for creating or updating an item.
    """
    name: str
    price: float
    is_available: bool = True


class ItemResponse(Item):
    """
    Schema for item response, including the database ID.
    """
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to work with ORM models