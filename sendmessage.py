# Example send message using Telegram bot
#
# Call from commandline with
# $ python sendmessage.py 'Hello world!'
#

import sys
from telegrambot import TelegramBot


def sendmessage(message):
    telegram_token = open('.tbot-token', 'r').readline().strip()
    try:
        telegram_chatid = open('.tbot-chatid', 'r').readline().strip()
    except FileNotFoundError:
        telegram_chatid = None

    bot = TelegramBot(telegram_token, telegram_chatid)

    resp = bot.sendmessage(message)
    if not resp['ok']:
        raise ConnectionError("Could not send message, error %s" % resp['description'])
    else:
        print("Message send!")


if __name__ == "__main__":
    message = sys.argv[1]
    sendmessage(message)
