from aiogram.utils.keyboard import InlineKeyboardBuilder



def prem_user_caption(chat_id: int):
    prem_user = InlineKeyboardBuilder()

    prem_user.button(text="Start update", callback_data=f"started:{chat_id}")
    prem_user.button(text="End update", callback_data=f"ended:{chat_id}")
    prem_user.button(text="Delete user", callback_data=f"deleted:{chat_id}")

    prem_user.adjust(1)
    return prem_user.as_markup()