from aiogram import Bot, Dispatcher, types
import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from register_handler.reg_callback import register_handlers_callback
from register_handler.reg_commands import register_handlers_commands
from register_handler.reg_message import register_handlers_message
#import openai


async def main():
    bot = Bot(token=TOKEN,
              parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    try:
        await register_handlers_commands(dp)
        await register_handlers_callback(dp)
        await register_handlers_message(dp)

        await dp.start_polling()
    except:
        await register_handlers_commands(dp)
        await register_handlers_callback(dp)
        await register_handlers_message(dp)

        await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())