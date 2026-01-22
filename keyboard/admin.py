from aiogram.utils.keyboard import InlineKeyboardBuilder

admin_kb = InlineKeyboardBuilder()

admin_kb.button(text="Xabar yuborish", callback_data="send_message")
admin_kb.button(text="Statistika", callback_data="statistika")

admin_kb.adjust(2)

admin_kb = admin_kb.as_markup()