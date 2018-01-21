import telepot, os

token = os.getenv('bot_token')
bot = telepot.Bot(token)

print("Enter the webhook url")

url = str(input())[:-1]

url = url + '/tg/webhook/'

print(bot.setWebhook(url))