from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True


class ItemResponse(Item):
    id: int

    class Config:
        from_attributes = True
