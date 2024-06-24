from app.database.models import SessionLocal
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id):
    async with SessionLocal() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            new_user = User(tg_id=tg_id)
            session.add(new_user)
            await session.commit()


async def get_category():
    async with SessionLocal() as session:
        return await session.scalars(select(Category))
    

async def get_item_by_category(category_id):
    async with SessionLocal() as session:
        return await session.scalars(select(Item).where(Item.category_id==category_id))


async def get_item(item_id):
    async with SessionLocal() as session:
        return await session.scalar(select(Item).where(Item.id==item_id))