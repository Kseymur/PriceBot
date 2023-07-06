from aiogram import Dispatcher, types

from State.wait_photo_nikora import WaitPhotoNikora
from State.wait_photo_universami import WaitPhotoUniversami
from handler.message import message_get_photo_nikora, message_get_photo_universami
from aiogram.dispatcher import FSMContext


async def register_handlers_message(dp: Dispatcher):
        dp.register_message_handler(message_get_photo_nikora, state=WaitPhotoNikora.wait_photo, content_types=['photo'])
        dp.register_message_handler(message_get_photo_universami, state=WaitPhotoUniversami.wait_photo, content_types=['photo'])
