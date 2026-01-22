from aiogram.fsm.state import StatesGroup, State

class PremiumUserUpdate(StatesGroup):
    start_update = State()
    end_update = State()
