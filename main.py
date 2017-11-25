import json
import random
import decimal
import functools
import sys

from ga import DisneyWorld
from gene import Human

sys.setrecursionlimit(7000)

MAX_GENES = 8000
MAX_GENERATION = 500
PROBABILITY_MUTATION = 0.1

LENGTH_GENE = 20
FREQUENCY_MUTATION = 0.2


def average(list_number):
    amount = functools.reduce(lambda x,y: x+y, list_number)
    length = len(list_number)
    return amount / length


def evolution(people, world, generation):

    print('\r\n>> Generation ', generation)

    # evaluate people with the world
    people_evaluated = []
    for p in people:
        people_evaluated.append(world.evaluate(p))

    evaluations = list(map(lambda x: x.getEvaluation(), people_evaluated))
    evaluations.sort(reverse=True)
    avg = average(evaluations)

    # result
    print('MAXIMAM EVALUATION: ', evaluations[0])
    print('MINIMAM EVALUATION: ', evaluations[-1])
    print('AVERAGE: ', avg)

    if(generation >= MAX_GENERATION):
        people_evaluated.sort(key=lambda x: x.getEvaluation(), reverse=True)
        return people_evaluated[0:5]

    print('\r\nAlternating generation...')

    people_next = []

    # cross over
    while(len(people) != 0):

        # cross over
        family = []
        len_people = len(people)
        family.append(people.pop(random.randrange(len_people)))
        len_people = len(people)
        family.append(people.pop(random.randrange(len_people)))
        children = family[0] * family[1]
        family.append(children[0])
        family.append(children[1])

        # selection
        for i in range(4):
            family[i] = world.evaluate(family[i])
        family.sort(key=lambda x: x.getEvaluation(), reverse=True)
        people_next.extend(family[:2])

    # mutation
    if((generation % 50) != 0):
        probability = PROBABILITY_MUTATION
    else:
        print('***********************************************************')
        probability = 0.9
    for p in people_next:
        if((random.randint(1, 100) / decimal.Decimal(100)) <= probability):
            p.mutate()

    # next generation
    result = evolution(people_next, world, generation+1)

    return result


if __name__ == '__main__':

    with open('./attractions.json', 'r') as f:
        data_attractions = json.load(f)

    disney_world = DisneyWorld(data_attractions["attractions"])
    print('A world named Disney has been created.')

    people = []
    # create people with random gene sequences
    for i in range(MAX_GENES):
        human = Human(LENGTH_GENE, data_attractions["number"]*2, FREQUENCY_MUTATION)
        human.generate()
        people.append(human)

    print(len(people), 'people enter the dream world today!')

    result = evolution(people, disney_world, 1) # continue evolution up to MAX_GENERATION

    print('\r\nEvolution has finished.\r\n\r\n---------- RESULT ----------')

    # print result
    for i in range(len(result)):
        print(i, ' >>')
        print('EVALUATION  : ', result[i].getEvaluation())
        print('GENESEQUENCE: ', result[i].getGeneSequence())

        print('ACTION:')

        for r in result[i].getGeneSequence():

            key = list(data_attractions["attractions"].keys())
            if(r < data_attractions["number"]):
                action = 'RIDE    '
                attraction = key[r]
            else:
                r -= data_attractions["number"]
                action = 'FASTPASS'
                attraction = key[r]

            print(action, ': ', attraction)
