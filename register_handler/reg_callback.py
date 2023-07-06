from aiogram import Dispatcher

from handler.callback import call_nikora, call_universami


async def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_nikora, lambda call: call.data =="nikora",state="*")
    dp.register_callback_query_handler(call_universami, lambda call: call.data =="universami",state="*")