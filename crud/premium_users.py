from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from models.models import PremiumUsers

tz = pytz.timezone("Asia/Tashkent")


async def get_or_create_or_extend_premium_user(
    session: AsyncSession,
    chat_id: int,
    months: int,
    file_id: str | None
) -> PremiumUsers:
    """
    Agar foydalanuvchi mavjud bo'lsa:
        - file_id yangilanadi (agar berilgan bo'lsa)
        - end_at oylari uzaytiriladi
    Agar foydalanuvchi mavjud bo'lmasa:
        - yangi Premium_Users yaratadi
    """
    result = await session.execute(
        select(PremiumUsers).where(PremiumUsers.chat_id == chat_id)
    )
    user = result.scalar_one_or_none()
    now = datetime.now(tz)
    now_ts = int(datetime.now(tz).timestamp())
    next_month = now + relativedelta(months=months)
    next_month_ts = int(next_month.timestamp())

    if user:
        if file_id:
            user.file_id = file_id

        update_month_dt = datetime.fromtimestamp(user.end_at, tz)
        update_month_ts = update_month_dt + relativedelta(months=months)
        user.end_at = int(update_month_ts.timestamp())

        session.add(user)
        await session.commit()
        await session.refresh(user)
    else:
        user = PremiumUsers(
            chat_id=chat_id,
            file_id=file_id,
            start_at=now_ts,
            end_at=next_month_ts
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user



async def get_expired_users(session):
    now_ts = int(datetime.now(tz).timestamp())
    # now_ts = 1770966593
    result = await session.execute(
        select(PremiumUsers).where(PremiumUsers.end_at <= now_ts)
    )
    return result.scalars().all()

async def delete_premium_user(session, chat_id: int):
    await session.execute(
        delete(PremiumUsers).where(PremiumUsers.chat_id == chat_id)
    )
    await session.commit()

async def all_premium_users(session):
    result = await session.execute(
        select(PremiumUsers)
    )
    return result.scalars().all()

async def get_one_premium_user(session, chat_id):
    result = await session.execute(
        select(PremiumUsers).where(PremiumUsers.chat_id == chat_id)
    )
    return result.scalar_one_or_none()

async def end_update_premium_user(session, chat_id, end_at):
    result = await session.execute(
        select(PremiumUsers).where(PremiumUsers.chat_id == chat_id)
    )
    user = result.scalar_one_or_none()
    if user:
        end_at_dt = datetime.strptime(end_at, "%Y-%m-%d %H:%M")
        end_at_ts = int(end_at_dt.timestamp())
        user.end_at = end_at_ts
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user

async def start_update_premium_user(session, chat_id, start_at):
    res = await session.execute(
        select(PremiumUsers).where(PremiumUsers.chat_id == chat_id)
    )
    user = res.scalar_one_or_none()
    if user:
        start_at_dt = datetime.strptime(start_at, "%Y-%m-%d %H:%M")
        start_at_ts = int(start_at_dt.timestamp())
        user.start_at = start_at_ts
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user



