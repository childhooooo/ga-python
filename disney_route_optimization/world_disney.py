
import functools
import decimal
import copy
import sys,os
sys.path.append(os.pardir + '/ga_base')

from human import Human
from human_guest import Guest
from world import World
from attraction import Attraction


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
