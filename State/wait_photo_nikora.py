from aiogram.dispatcher.filters.state import StatesGroup, State


class WaitPhotoNikora(StatesGroup):
    wait_photo = State()