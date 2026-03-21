from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.item import Item, ItemResponse
from app.crud import item as crud
from app.core.database import get_db

router = APIRouter()


@router.post("/items", response_model=ItemResponse)
async def create_item(item: Item, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to create a new item (Async).
    """
    return await crud.create_item(db, item)


@router.get("/items", response_model=list[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve all items (Async).
    """
    return await crud.get_items(db)


@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve a specific item by ID (Async).
    """
    item = await crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to delete an item by ID (Async).
    """
    item = await crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
