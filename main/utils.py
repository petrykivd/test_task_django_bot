import asyncio
from os import getenv

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


async def send_message_to_user(user_id, text) -> None:
    bot = Bot(TOKEN)
    try:
        await bot.send_message(chat_id=user_id, text=text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await bot.session.close()


def send_message_sync(user_id, text):
    asyncio.run(send_message_to_user(user_id, text))