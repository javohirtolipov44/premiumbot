from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import User

# 🔍 READ (chat_id orqali)
async def get_user_by_chat_id(session: AsyncSession, chat_id: int) -> User | None:
    result = await session.execute(
        select(User).where(User.chat_id == chat_id)
    )
    return result.scalar_one_or_none()


# 🔄 GET or CREATE (eng ko‘p ishlatiladi)
async def get_or_create_user(session: AsyncSession, chat_id, full_name, username) -> User:
    result = await session.execute(
        select(User).where(User.chat_id == chat_id)
    )
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            chat_id=chat_id,
            full_name=full_name,
            username=username,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user


# ❌ DELETE
async def delete_user_by_chat_id(session: AsyncSession, chat_id: int):
    await session.execute(
        delete(User).where(User.chat_id == chat_id)
    )
    await session.commit()

# ✏️ UPDATE (file_id ni almashtirish kerak bo‘lsa)
async def update_user_file_id(session: AsyncSession, chat_id: int, new_file_id: str):
    await session.execute(
        update(User)
        .where(User.chat_id == chat_id)
        .values(file_id=new_file_id)
    )
    await session.commit()


# 📊 COUNT (statistika uchun)
async def get_all_users(session: AsyncSession):
    result = await session.execute(select(User))
    return result.scalars().all()
