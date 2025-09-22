from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from hermanitto_docs_api.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    async with SessionLocal() as session:
        yield session
