import os
import telepot, uuid
from app.api.create_auth_token import create
from app.bot.commands import telegram_command

TOKEN = os.getenv('bot_token')
bot = telepot.Bot(TOKEN)


@telegram_command('/login')
def login(msg):
    res = create(msg['chat']['id'])
    if res:
        bot.sendMessage(msg['chat']['id'], f'{os.getenv("domain")}/login/{res["token"]}')