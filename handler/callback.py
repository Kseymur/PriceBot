from aiogram import types
from aiogram.dispatcher import FSMContext

from State.wait_photo_nikora import WaitPhotoNikora
from State.wait_photo_universami import WaitPhotoUniversami


async def call_nikora(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправь фото ценника. Старайся сделать так, чтобы в кадр попал ценник только того товара, который тебя интересует, а изображение было чётким')
    await state.set_state(WaitPhotoNikora.wait_photo.state)
    print("nikora")


async def call_universami(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправь фото ценника. Старайся сделать так, чтобы в кадр попал ценник только того товара, который тебя интересует, а изображение было чётким')
    await state.set_state(WaitPhotoUniversami.wait_photo.state)
    print("universami")
