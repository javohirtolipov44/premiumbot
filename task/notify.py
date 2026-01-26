import asyncio
from datetime import datetime
import pytz
from aiogram import Bot

from config import ADMINS, NOTIFY_DATA, SERVER_PRICE, PROGRAMMER

tz = pytz.timezone("Asia/Tashkent")

async def monthly_admin_notify(bot: Bot):
        while True:
            now = datetime.now(tz)

            # Agar bugun 20-sana bo‘lsa
            if now.day == NOTIFY_DATA:
                for ADMIN in ADMINS:
                    try:
                        await bot.send_message(
                        ADMIN,
                        f"<b>📅 Bugun oyning {NOTIFY_DATA}-sanasi!\n"
                        f"🧾 Serverga pul to'lang: {SERVER_PRICE} so'm\n\n"
                        f"Aloqa uchun: @{PROGRAMMER}</b>",
                        parse_mode="html"
                        )
                    except Exception as e:
                        print(e)

                # ❗ Takror yubormaslik uchun 1 kun uxlaydi
                await asyncio.sleep(60 * 60 * 24)

            # Har 1 soatda tekshiradi
            await asyncio.sleep(60 * 60 * 2)