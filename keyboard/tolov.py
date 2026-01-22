from aiogram.utils.keyboard import InlineKeyboardBuilder

tolov_kb = InlineKeyboardBuilder()

tolov_kb.button(text="✅TO'LOV QILISH✅", callback_data="tolov")


tolov_kb.adjust(1)

tolov_kb = tolov_kb.as_markup()

obuna_kb = InlineKeyboardBuilder()

obuna_kb.button(text="OBUNA UZAYTIRISH", callback_data="tolov")


obuna_kb.adjust(1)

obuna_kb = obuna_kb.as_markup()