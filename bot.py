import logging, asyncio, sys, os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from handlers.user_handlers import user_router
from db.db import create_user_db
from keyboards.main_menu import main_menu


async def main():
    db = await create_user_db()
    bot: Bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    dp: Dispatcher = Dispatcher()
    dp.include_router(user_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=main_menu, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=['message', 'edited_message', 'callback_query'])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
