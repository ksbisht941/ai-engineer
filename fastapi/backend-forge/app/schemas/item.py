"""
Pydantic schemas for data validation and serialization.
"""
from pydantic import BaseModel

class Item(BaseModel):
    """
    Base schema for an Item, used for data input (creation/update).
    """
    name: str
    price: float
    is_available: bool = True


class ItemResponse(Item):
    """
    Schema for the response sent back to the client.
    Includes the database 'id' and enables ORM compatibility.
    """
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy objects
