# -*- coding: utf-8 -*-
import numpy as np
from CONFIG import SONGS
import os

class Bot:

    def __init__(self, bot, chat_id):
        self.bites = 0
        self.bot = bot
        self.chat_id = chat_id

    def bite(self, intended=0):
        self.bites += 1

        if intended == 0:
            base = np.random.choice(
                [
                    "Время нового укуса!",
                    "Соскучилась по укусам?",
                    "Хорошо себя ведешь? Едва ли!",
                    "Время кусалки!",
                    "Пора поточить зубки!",
                    "Синяки проходят?",
                ])
        else:
            base = "Я тебя не понял. За это - новый укус!"

        afterall = "Итого, по прибытию Айжан получит"

        if self.bites % 10 in [0, 2, 3, 4]:
            text = "{} {} {} укуса.".format(base, afterall, self.bites)
        elif self.bites % 10 in [1]:
            text = "{} {} {} укус.".format(base, afterall, self.bites)
        else:
            text = "{} {} {} укусов.".format(base, afterall, self.bites)

        if self.bites > 5 and self.bites < 20:
            text = "{} {} {} укусов".format(base, afterall, self.bites)



        self.bot.sendMessage(chat_id=self.chat_id, text=text)


    def song(self):
        if np.random.rand() > 0.8:
            song = "You and me - LifeHouse. Неразделенная любовь"
        else:
            song = np.random.choice(SONGS)

        self.bot.sendMessage(chat_id=self.chat_id, text="{}. Наслаждайся!".format(song))


    def miss(self, intended=0):

        if intended == 0:

            base = [
                    "Давно я тебе не говорил, как соскучился, неправда ли?",
                    "Айжан, я так скучаю! А ты?",
                    "Здесь совершенно некого кусать.",
                    "Возвращайся скорее! Тут все краски без тебя потеряли цвет!"
                    ]
        else:

            base = [
                "О, Айжан, ну ты что? Разумеется, я очень соскучился!",
                "Как можно не скучать по тебе?",
                "Знаешь чем я сейчас занимаюсь? Сижу и скучаю по Вас!",
            ]


        text = np.random.choice(base)

        if np.random.rand() > 0.5:
            photo_id = np.random.choice([1,2,3,4,5])
            message = self.bot.sendPhoto(
                photo=open(os.getcwd() + os.sep + 'Engine' + os.sep + 'Photos/{}.jpg'.format(photo_id), 'rb'),
                caption=text,
                chat_id=self.chat_id)
        else:
            self.bot.sendMessage(chat_id=self.chat_id, text=text)


    def scary(self):
        message = self.bot.sendPhoto(
            photo=open(os.getcwd() + os.sep + 'Engine' + os.sep + 'Photos/scary.jpg', 'rb'),
            caption="Буууууууу",
            chat_id=self.chat_id)




