import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_tg_message(text: str):
    bot = Bot(token=BOT_TOKEN)
    asyncio.run(bot.send_message(chat_id=BOT_ID, text=text))
