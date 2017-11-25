import random
import decimal
import copy

from functools import reduce

class Human(object):

    def __init__(self, length, width, frequency_mutation):
        self.gene_sequence = []
        self.evaluation = 0
        self.length = length
        self.width = width
        self.frequency_mutation = frequency_mutation


    def generate(self):
        self.gene_sequence.clear()
        for i in range(self.length):
            g = random.randrange(self.width)
            self.gene_sequence.append(g)


    def reset(self):
        self.evaluation = 0


    def evaluated(self, val):
       self.evaluation += val


    def mutate(self):
        for i in range(self.length):
            if((random.randint(1, 100) / decimal.Decimal(100)) <= self.frequency_mutation):
                self.gene_sequence[i] = random.randrange(self.width)

    '''
    def mutate(self):
        for i in range(self.length):
            if((random.randint(1, 100) / decimal.Decimal(100)) <= self.frequency_mutation):
                if(self.gene_sequence[i] < (self.width // 2)):
                    self.gene_sequence[i] += (self.width // 2)
                else:
                    self.gene_sequence[i] -= (self.width //2)
    '''

    '''
    def mutate(self):
        position = [random.randrange(self.length), random.randrange(self.length)]
        position.sort()
        part = copy.deepcopy(self.gene_sequence[position[0] : position[1]])
        self.gene_sequence[position[0] : position[1]] = []
        point_insert = random.randrange(len(self.gene_sequence))
        self.gene_sequence[point_insert : point_insert] = part
    '''

    def __mul__(self, other):
        position = [random.randrange(self.length), random.randrange(self.length)]
        position.sort()
        son = Human(self.length, self.width, self.frequency_mutation)
        son.setGeneSequence(copy.deepcopy(self.getGeneSequence()))
        daughter = Human(self.length, self.width, self.frequency_mutation)
        daughter.setGeneSequence(copy.deepcopy(other.getGeneSequence()))

        for i in range(position[0], position[1]):
            son.setGene(i, other.getGene(i))
            daughter.setGene(i, self.getGene(i))

        return [son, daughter]


    '''
    def __mul__(self, other):
        position = [random.randrange(self.length), random.randrange(self.length)]
        position.sort()
        son = Human(self.length, self.width, self.frequency_mutation)
        son.setGeneSequence(copy.deepcopy(self.getGeneSequence()))
        daughter = Human(self.length, self.width, self.frequency_mutation)
        daughter.setGeneSequence(copy.deepcopy(other.getGeneSequence()))

        for i in range(self.length // 2):
            if(random.randrange(100) < 50):
                son.setGene(i*2, other.getGene(i*2))
                daughter.setGene(i*2, self.getGene(i*2))

        return [son, daughter]
    '''


    def getEvaluation(self):
        return self.evaluation


    def setGeneSequence(self, gene_sequence):
        self.gene_sequence = gene_sequence


    def getGeneSequence(self):
        return self.gene_sequence


    def setGene(self, position, value):
        self.gene_sequence[position] = value


    def getGene(self, position):
        return self.gene_sequence[position]



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

