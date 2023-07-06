from aiogram import Dispatcher

from handler.commands import cmd_start


async def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"], state="*")

