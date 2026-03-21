"""
API route definitions for the application.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

# Initialize the API router
router = APIRouter()


@router.post("/items", response_model=schemas.ItemResponse)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    """
    Endpoint to create a new item.
    """
    return crud.create_item(db, item)


@router.get("/items", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all items.
    """
    return crud.get_items(db)


@router.get("/items/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a specific item by ID.
    """
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete an item by ID.
    """
    item = crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}