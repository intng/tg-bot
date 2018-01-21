import os
import telepot, uuid
from app.postgres import regs
from app.bot.commands import telegram_command

TOKEN = os.getenv('bot_token')
bot = telepot.Bot(TOKEN)


@telegram_command('/reg')
def reg(msg):
    token = msg['text'].split(" ")[1]
    if 'last_name' in msg['chat']:
        surname = msg['chat']['lastname']
    else:
        surname = None
    if not regs.check_reg(token):
        bot.sendMessage(msg['chat']['id'], 'Неправильный код')
        return
    if regs.update(msg['chat']['id'], msg['chat']['first_name'], token, surname):
        bot.sendMessage(msg['chat']['id'], 'Успешно подтверждено!')
        return
    else:
        bot.sendMessage(msg['chat']['id'], 'Неправильный код')
        return
