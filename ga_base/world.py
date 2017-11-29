
import functools
import decimal
import copy

from human import Human


class World(object):

    def __init__(self):
        return


    def evaluate(self, human):
        amount = functools.reduce(lambda x,y: x+y, human.getGeneSequence())
        length = human.length
        h = copy.deepcopy(human)
        h.reset()
        h.evaluated(amount / decimal.Decimal(length))
        return h
