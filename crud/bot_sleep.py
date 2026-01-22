from datetime import datetime

import pytz
from dateutil.relativedelta import relativedelta
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import BotSleep

tz = pytz.timezone("Asia/Tashkent")

async def create_or_update(session: AsyncSession, sleep_time: int) -> BotSleep:

    result = await session.execute(
        select(BotSleep).limit(1)
    )
    bot_sleep = result.scalar_one_or_none()
    if not bot_sleep:
        now = datetime.now(tz)
        next_hour = now + relativedelta(hours=sleep_time)
        next_hour_ts = int(next_hour.timestamp())
        bot_sleep = BotSleep(
            sleep_time=next_hour_ts,
        )
    else:
        now = datetime.fromtimestamp(bot_sleep.sleep_time, tz)
        next_hour = now + relativedelta(hours=sleep_time)
        next_hour_ts = int(next_hour.timestamp())
        bot_sleep.sleep_time = next_hour_ts
    session.add(bot_sleep)
    await session.commit()
    await session.refresh(bot_sleep)

    return bot_sleep

async def delete_bot_sleep(session: AsyncSession):
    await session.execute(
        delete(BotSleep)
    )
    await session.commit()

async def count_bot_sleep(session: AsyncSession) -> int:
    result = await session.execute(select(BotSleep))
    return len(result.scalars().all())

async def get_bot_sleep(session: AsyncSession):
    result = await session.execute(
        select(BotSleep).limit(1)
    )
    bot_sleep = result.scalar_one_or_none()
    return bot_sleep
