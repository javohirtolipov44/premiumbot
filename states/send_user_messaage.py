from aiogram.fsm.state import StatesGroup, State

class SendUserMessageState(StatesGroup):

    send_user_message = State()