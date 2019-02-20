from os import listdir
from random import shuffle
import numpy as np

from research.article import Article


class Load:

    @staticmethod
    def load():
        return Load.numpify(Load.raw())

    @staticmethod
    def raw():
        tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        articles = []
        for tag in tags:
            files = listdir('/home/ms10596/Documents/match/research/CEFR/' + tag)
            for i in files:
                f = open('/home/ms10596/Documents/match/research/CEFR/' + tag + '/' + i)
                article = f.read()
                articles.append(Article(article, tags.index(tag)))
        return articles

    @staticmethod
    def numpify(articles):
        shuffle(articles)
        x = np.empty(shape=(len(articles), 12))
        y = np.empty(shape=(len(articles), 1), dtype=object)
        for i in range(len(articles)):
            ff = FeaturesFactory(articles[i])
            x[i][0] = ff.avg_sentence_length()
            x[i][1] = ff.avg_word_length()
            x[i][2] = ff.adj()
            x[i][3] = ff.adv()
            x[i][4] = ff.article()
            x[i][5] = ff.conjunctions()
            x[i][6] = ff.interjections()
            x[i][7] = ff.nouns()
            x[i][8] = ff.numerals()
            x[i][9] = ff.past_participle()
            x[i][10] = ff.pronouns()
            x[i][11] = ff.special_symbols()

            y[i] = ff.tag
        return x, y

    @staticmethod
    def divide(x, y):
        portion = int(0.8 * len(x))
        x_train = x[:portion]
        y_train = y[:portion]

        x_test = x[portion:]
        y_test = y[portion:]

        return x_train, y_train, x_test, y_test

# print(Load.load())
# print(__file__)