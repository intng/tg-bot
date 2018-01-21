from venusian import Scanner

from app.bot import commands

commands_mapping = {}


def telegram_command(command: str):
    """
    Decorator which registers telegram command handlers
    :param command: The command from which user message should be started to be routed to this handler,including slash
                    e.g. "/start" or "/login"
    """
    def decorator(fn):
        commands_mapping[command] = fn
        return fn
    return decorator


Scanner().scan(commands)
pass