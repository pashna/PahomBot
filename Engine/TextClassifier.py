# -*- coding: utf-8 -*-

class TextClassifier:

    MUSIC = 0
    MISS = 1
    SCARY = 2
    BITE = 3

    def __init__(self):
        pass

    def classify(self, text):
        text = text.lower()
        if u'песн' in text \
           or u'музык' in text \
           or u'песе' in text\
           or u'мелод' in text:
            return TextClassifier.MUSIC

        elif u'ску' in text:
            return TextClassifier.MISS

        elif u'пуг' in text or u'стра' in text:
            return TextClassifier.SCARY

        else:
            return TextClassifier.BITE
