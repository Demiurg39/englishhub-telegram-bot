from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.englishhub_bot.config import settings
from src.englishhub_bot.database.models import Base

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.ECHO_SQL,
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

async def get_db_session() -> AsyncSession:
    """Dependency for getting a DB session."""
    async with async_session_factory() as session:
        yield session

async def init_db():
    """Create tables (useful for dev/sqlite)."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
