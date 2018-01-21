from app.bot.commands import commands_mapping

def update(upd):
    message = upd['message']
    if message['chat']['type'] == 'private':
        cmd_str = message['text'].split(" ")[0]
        if cmd_str in commands_mapping:
            command = commands_mapping[cmd_str]
            command(message)
        else:
            pass