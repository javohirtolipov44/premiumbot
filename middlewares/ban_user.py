from datetime import datetime

import pytz
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Awaitable, Callable, Any, Dict
from crud.ban_users import get_one_ban_user
from database import async_session

tz = pytz.timezone("Asia/Tashkent")

class BanUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:


        user_id = event.from_user.id
        async with async_session() as session:
            ban_users = await get_one_ban_user(session, user_id)

        if ban_users:
            ban_time_dt = datetime.fromtimestamp(ban_users.ban_time, tz)
            ban_time = ban_time_dt.strftime("%d.%m.%Y")
            await event.answer("<b>Endi botdan ko'rsatilgan vaqt kelmaguncha foydalana olmaysiz.\n\n"
                                        f"{ban_time}</b>",
                                       parse_mode="HTML")
            return None
        return await handler(event, data)