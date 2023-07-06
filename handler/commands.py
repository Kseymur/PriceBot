from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def cmd_start(message: types.Message, state: FSMContext):
    inline_kb = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton("Nikora", callback_data="nikora"),
               InlineKeyboardButton("Universami", callback_data="universami")]
    inline_kb.add(*buttons)
    await message.answer("Привет! Я конвертирую для тебя цены с грузинских ценников. Выбери нужный магазин",
                         reply_markup=inline_kb)


