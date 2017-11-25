from gene import Human
from gene import Guest
from attraction import Attraction

import functools
import decimal
import copy

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


class DisneyWorld(World):

    def __init__(self, attractions):
        super().__init__()
        self.attractions = []
        for k, v in attractions.items():
            self.attractions.append(Attraction(k, v["value"], v["latency"], v["fastpass"]))


    def evaluate(self, human):

        g = Guest(human.length, human.width, human.frequency_mutation)
        g.setGeneSequence(copy.deepcopy(human.getGeneSequence()))

        for s in g.getGeneSequence():

            if(s < len(self.attractions)):
                result = self.attractions[s].ride(g)
                g.spend(result[0])
                g.evaluated(result[1])

            else:
                result = self.attractions[s - len(self.attractions)].ticket(g)
                g.spend(result[0])
                g.getFastpass(result[1])

        h = Human(human.length, human.width, human.frequency_mutation)
        h.setGeneSequence(copy.deepcopy(g.getGeneSequence()))
        h.evaluated(g.getEvaluation())

        return h
