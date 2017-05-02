# -*- coding: utf-8 -*-

from telegram.ext import Updater
from CONFIG import TOKEN
from Engine.Bot import Bot
from telegram.ext import CommandHandler
from time import sleep
from telegram.ext import MessageHandler, Filters
from Engine.TextClassifier import TextClassifier
import numpy as np


bots = []
chatid_bot_map = {}

def start(bot, update):
    chat_id = update.message.chat_id
    mybot = Bot(bot, chat_id)

    if chat_id in chatid_bot_map:
        bot.sendMessage(chat_id=chat_id, text="Ты меня не проведешь!")
        chatid_bot_map[chat_id].bot = bot
    else:
        bots.append(mybot)
        chatid_bot_map[chat_id] = mybot
        bot.sendMessage(chat_id=chat_id, text="Теперь я буду твоим Пахомчиком!")

def reply(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    bot = chatid_bot_map[chat_id]

    clf = TextClassifier()
    type = clf.classify(text)
    if type == TextClassifier.MUSIC:
        bot.song()
    elif type == TextClassifier.MISS:
        bot.miss(intended=1)
    elif type == TextClassifier.SCARY:
        bot.scary()
    elif type == TextClassifier.BITE:
        bot.bite(intended=1)

if __name__ == '__main__':

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

    while True:
        try:
            timeout = 20
            sleep(timeout)
            for b in bots:
                rand = np.random.rand()
                if rand < 0.6:
                    b.bite()

                if rand > 0.6 and rand < 0.7:
                    b.miss()

                if rand > 0.7 and rand < 0.95:
                    b.song()

                if rand > 0.95:
                    b.scary()

        except Exception:
            pass