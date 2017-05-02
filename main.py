from telegram.ext import Updater

updater = Updater(token='267022894:AAHCdlT0MVUq9zP7efxt0jf7NUDMcs2HaFc')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")