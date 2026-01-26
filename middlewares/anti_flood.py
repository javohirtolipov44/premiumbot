import time
from config import ADMINS
from collections import defaultdict
from aiogram import BaseMiddleware
from aiogram.types import Message

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, limit=10, window=60, block_time=600):
        self.limit = limit          # nechta xabar
        self.window = window        # necha sekund ichida
        self.block_time = block_time  # blok vaqti

        self.user_messages = defaultdict(list)
        self.blocked_users = {}

    async def __call__(self, handler, event: Message, data):
        if not isinstance(event, Message):
            return await handler(event, data)

        user_id = event.from_user.id

        # ✅ Adminlar o‘tkazib yuboriladi
        if user_id in ADMINS:
            return await handler(event, data)

        now = time.time()

        # ⛔ Bloklangan bo‘lsa
        if user_id in self.blocked_users:
            if now < self.blocked_users[user_id]:
                await event.answer("🚫 Flood qilyapsiz! Biroz kuting.")
                return
            else:
                del self.blocked_users[user_id]

        # Eski vaqtlarni tozalash
        self.user_messages[user_id] = [
            t for t in self.user_messages[user_id]
            if now - t < self.window
        ]

        self.user_messages[user_id].append(now)

        # ⚠ Limitdan oshsa blok
        if len(self.user_messages[user_id]) > self.limit:
            self.blocked_users[user_id] = now + self.block_time
            await event.answer("⏳ Juda tez yozdingiz! 10 daqiqa bloklandingiz.")
            return

        return await handler(event, data)
