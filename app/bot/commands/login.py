import os
import telepot, uuid
from app.bot.commands import telegram_command

TOKEN = os.getenv('bot_token')
bot = telepot.Bot(TOKEN)

@telegram_command('/login')
def login(msg):
    