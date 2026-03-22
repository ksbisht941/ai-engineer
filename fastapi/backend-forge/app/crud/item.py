"""
CRUD (Create, Read, Update, Delete) operations for the Item model.
These functions handle all direct interactions with the database.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.item import ItemDB
from app.schemas.item import Item


async def create_item(db: AsyncSession, item: Item):
    """
    Asynchronously creates a new item in the database.
    """
    db_item = ItemDB(**item.dict())
    db.add(db_item)
    await db.commit()         # Save changes
    await db.refresh(db_item)  # Get the generated 'id' from the DB
    return db_item


async def get_items(db: AsyncSession):
    """
    Asynchronously retrieves all items from the database.
    """
    result = await db.execute(select(ItemDB))
    return result.scalars().all()


async def get_item(db: AsyncSession, item_id: int):
    """
    Asynchronously retrieves a single item by its ID.
    """
    result = await db.execute(
        select(ItemDB).where(ItemDB.id == item_id)
    )
    return result.scalar_one_or_none()


async def delete_item(db: AsyncSession, item_id: int):
    """
    Asynchronously deletes an item from the database.
    """
    item = await get_item(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()
    return item
