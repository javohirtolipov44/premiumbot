from datetime import datetime

import pytz
from dateutil.relativedelta import relativedelta
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import BanUsers

tz = pytz.timezone("Asia/Tashkent")

async def create_or_update_ban_user(session: AsyncSession, chat_id, ban_time) -> BanUsers:

    result = await session.execute(
        select(BanUsers).where(BanUsers.chat_id == chat_id)
    )
    ban_user = result.scalar_one_or_none()
    if not ban_user:
        now = datetime.now(tz)
        next_hour = now + relativedelta(days=ban_time)
        next_hour_ts = int(next_hour.timestamp())
        ban_user = BanUsers(
            chat_id=chat_id,
            ban_time=next_hour_ts,
        )
    else:
        ban_time_db = datetime.fromtimestamp(ban_user.ban_time, tz)
        next_hour = ban_time_db + relativedelta(days=ban_time)
        next_hour_ts = int(next_hour.timestamp())
        ban_user.ban_time = next_hour_ts
    session.add(ban_user)
    await session.commit()
    await session.refresh(ban_user)

    return ban_user

async def get_all_ban_users(session: AsyncSession):
    result = await session.execute(
            select(BanUsers)
    )
    return result.scalars().all()

async def get_one_ban_user(session: AsyncSession, chat_id: int) -> BanUsers:
    result = await session.execute(
        select(BanUsers).where(BanUsers.chat_id == chat_id)
    )
    ban_user = result.scalar_one_or_none()
    return ban_user

async def delete_ban_user(session: AsyncSession, chat_id):
    result = await session.execute(
        select(BanUsers).where(BanUsers.chat_id == chat_id)
    )
    ban_user = result.scalar_one_or_none()
    if not ban_user:
        return False
    await session.execute(
        delete(BanUsers)
        .where(BanUsers.chat_id == chat_id)
    )
    await session.commit()
    return True
