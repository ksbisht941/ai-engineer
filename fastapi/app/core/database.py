"""
Asynchronous database setup using SQLAlchemy with the asyncpg driver.
"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# Create the asynchronous engine to handle database connections
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,           # Set to True if you want to see SQL queries in the logs
    pool_pre_ping=True    # Ensures connections are still alive before using them
)

# Factory for creating asynchronous database sessions
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for all database models (ItemDB, etc.)
Base = declarative_base()


async def get_db():
    """
    Dependency generator to yield an async database session for every request.
    This ensures the session is properly closed after usage.
    """
    async with AsyncSessionLocal() as session:
        yield session
