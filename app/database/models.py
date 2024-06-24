from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from config import read_config


config = read_config()
engine = create_async_engine(config.DATABASE_URL)
Base = declarative_base()
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def db_connect():
    async with SessionLocal() as session:
        yield session


async def db_disconnect():
    await engine.dispose()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Item(Base):
    __tablename__ = 'items'


    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(200))
    price = Column(Integer)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)


