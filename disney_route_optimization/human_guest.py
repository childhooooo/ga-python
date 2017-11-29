
import random
import decimal
import copy
from functools import reduce
import sys,os
sys.path.append(os.pardir + '/ga_base')

from human import Human


class Guest(Human):

    def __init__(self, length, width, frequency_mutation):
        super().__init__(length, width, frequency_mutation)
        self.tickets = []
        self.gotTicket = -121
        self.clock = 0


    def reset(self):
        self.evaluation = 0
        self.clock = 0


    def now(self):
        return self.clock


    def spend(self, time):
        self.clock += time


    def getFastpass(self, fastpass):
        self.tickets.append(fastpass)
        self.gotTicket = self.now()


    def showTickets(self):
        return self.tickets


    def lastTimeGotTicket(self):
        return self.gotTicket

