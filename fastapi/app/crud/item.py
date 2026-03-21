from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.item import ItemDB
from app.schemas.item import Item


async def create_item(db: AsyncSession, item: Item):
    db_item = ItemDB(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def get_items(db: AsyncSession):
    result = await db.execute(select(ItemDB))
    return result.scalars().all()


async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(
        select(ItemDB).where(ItemDB.id == item_id)
    )
    return result.scalar_one_or_none()


async def delete_item(db: AsyncSession, item_id: int):
    item = await get_item(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()
    return item
