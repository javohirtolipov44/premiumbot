from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/premiumbot"

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def check_db_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ PostgreSQL ga muvaffaqiyatli ulandi")
        return True
    except Exception as e:
        print("❌ PostgreSQL ga ulanishda xatolik:", e)
        return False


async def create_tables():
    # Modellarni import qilish
    from models.models import User, PremiumUsers

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Jadval(lar) yaratildi")