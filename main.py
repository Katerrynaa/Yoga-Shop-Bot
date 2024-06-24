import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import db_disconnect, db_connect


async def main():
    async for session in db_connect():
        bot = Bot(token='7266877781:AAEUb-Sf39LnIvxpzzt2y6PpO7grzXMIDiM')
        dp = Dispatcher()
        dp.include_router(router)
        
        try:
            await dp.start_polling(bot)
        finally:
            await db_disconnect(session)

async def db_disconnect(session):
    await session.close()


if __name__ == '__main__':
    asyncio.run(main())