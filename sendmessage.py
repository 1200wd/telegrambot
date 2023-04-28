#!/usr/bin/python

# Example send message using Telegram bot

import sys
from telegrambot import TelegramBot


telegram_token = open('.token', 'r').readline().strip()
message = sys.argv[1]

bot = TelegramBot(telegram_token)

resp = bot.sendmessage(message)
if not resp['ok']:
    raise ConnectionError("Could not send message, error %s" % resp['description'])
else:
    print("Message send!")
