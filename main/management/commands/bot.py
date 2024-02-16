import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from channels.db import database_sync_to_async
from django.core.management import BaseCommand
from dotenv import load_dotenv

from main.models import User

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    if await user_exists(message):
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    else:
        await register_user(message)
        await message.answer(f"Welcome, {hbold(message.from_user.full_name)}!")
        await message.answer("Registration successful 👍")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("It is being developed 👨‍💻")


async def main(bot) -> None:
    await dp.start_polling(bot)


@database_sync_to_async
def user_exists(message):
    if User.objects.filter(tg_user_id=message.from_user.id).exists():
        return True
    return False


@database_sync_to_async
def register_user(message):
    tg_user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    User.objects.create(
        tg_user_id=tg_user_id,
        username=username,
        first_name=first_name
    )


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main(bot=bot))

