# -*- coding: utf-8 -*-

from telegram.ext import Updater
from CONFIG import TOKEN, TIMEOUT
from Engine.Bot import Bot
from telegram.ext import CommandHandler
from time import sleep
from telegram.ext import MessageHandler, Filters
from Engine.TextClassifier import TextClassifier
import numpy as np
import logging
import encodings

bots = []
chatid_bot_map = {}

def start(bot, update):
    chat_id = update.message.chat_id
    mybot = Bot(bot, chat_id)
    logging.error("START. {}".format(chat_id))

    if chat_id in chatid_bot_map:
        bot.sendMessage(chat_id=chat_id, text="Ты меня не проведешь!")
        chatid_bot_map[chat_id].bot = bot
    else:
        bots.append(mybot)
        chatid_bot_map[chat_id] = mybot
        bot.sendMessage(chat_id=chat_id, text="Теперь я буду твоим Пахомчиком!")

def reply(bot_, update):
    chat_id = update.message.chat_id

    if chat_id not in chatid_bot_map:
        chatid_bot_map[chat_id] = Bot(bot_, chat_id)
    try:
        text = update.message.text
        bot = chatid_bot_map[chat_id]

        logging.error(u"MSG from chat_id={}. {}".format(chat_id, text) )

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

    except Exception as e:
        logging.exception(e)
        bot_.sendMessage(chat_id=chat_id, text="")

if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename= "telegram_bot.log")

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, reply)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

    while True:
        try:
            timeout = TIMEOUT * np.random.rand()
            sleep(timeout)
            for b in bots:
                rand = np.random.rand()
                if rand < 0.6:
                    b.bite()

                if rand > 0.6 and rand < 0.75:
                    b.miss()

                if rand > 0.75 and rand < 0.95:
                    b.song()

                if rand > 0.95:
                    b.scary()

        except Exception as e:
            logging.exception(e)