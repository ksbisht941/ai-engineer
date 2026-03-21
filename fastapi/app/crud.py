"""
CRUD (Create, Read, Update, Delete) operations for the database.
"""
from sqlalchemy.orm import Session
from app import models, schemas


def create_item(db: Session, item: schemas.Item):
    """
    Create a new item in the database.
    """
    db_item = models.ItemDB(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session):
    """
    Retrieve all items from the database.
    """
    return db.query(models.ItemDB).all()


def get_item(db: Session, item_id: int):
    """
    Retrieve a specific item by its ID.
    """
    return db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()


def delete_item(db: Session, item_id: int):
    """
    Delete an item from the database.
    """
    item = get_item(db, item_id)
    if item:
        db.delete(item)
        db.commit()
    return item