from aiogram.filters.callback_data import CallbackData

class MediaCallback(CallbackData, prefix="media"):
    chat_id: int
    months: int
