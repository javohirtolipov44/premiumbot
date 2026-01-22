from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import KARTA_NUMBER

karta_kb = InlineKeyboardBuilder()

karta_kb.button(text="✅KARTA MA'LUMOTLARI✅", callback_data="", url=f"{KARTA_NUMBER}")


karta_kb.adjust(1)

karta_kb = karta_kb.as_markup()