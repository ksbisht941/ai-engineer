"""
API route definitions for the Item resource.
This layer maps HTTP endpoints to CRUD operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.item import Item, ItemResponse
from app.crud import item as crud
from app.core.database import get_db

# Create a router for item-related endpoints
router = APIRouter()


@router.post("/items", response_model=ItemResponse)
async def create_item(item: Item, db: AsyncSession = Depends(get_db)):
    """
    Route to create a new item.
    Uses 'Depends(get_db)' to inject an async database session.
    """
    return await crud.create_item(db, item)


@router.get("/items", response_model=list[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    """
    Route to retrieve all items.
    """
    return await crud.get_items(db)


@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Route to retrieve a specific item by its ID.
    Raises a 404 error if the item is not found.
    """
    item = await crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Route to delete an item.
    """
    item = await crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
