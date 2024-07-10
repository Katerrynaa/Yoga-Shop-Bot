import os
from logging.config import fileConfig
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from alembic import context


load_dotenv()

config = context.config
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))


if config.config_file_name:
    fileConfig(config.config_file_name)


from app.database.models import Base

target_metadata = Base.metadata


def run_migrations_online() -> None:
    connectable = AsyncEngine(engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    ))

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    raise NotImplementedError("Offline mode not supported")
else:
    from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
    from sqlalchemy.orm import sessionmaker

   
    async def async_main():
        async with create_async_engine(os.environ["DATABASE_URL"], echo=True) as engine:
            async with engine.connect() as conn:
                await conn.run_sync(Base.metadata.create_all)
                async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

                async with async_session() as session:
                    yield session






