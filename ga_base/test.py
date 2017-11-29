
import json
import random
import decimal
import functools

from world import World
from human import Human

MAX_GENES = 100
MAX_GENERATION = 100
PROBABILITY_MUTATION = 0.01

LENGTH_GENE = 100
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
        return people_evaluated[0].getGeneSequence()

    print('Alternating generation...')

    people_next = []

    # cross over
    while(len(people) > 1):

        # cross over
        family = []
        position = random.randrange(len(people))
        family.append(people.pop(position))
        position = random.randrange(len(people))
        family.append(people.pop(position))
        children = family[0] * family[1]
        family.append(children[0])
        family.append(children[1])

        # selection
        for i in range(4):
            family[i] = world.evaluate(family[i])
        family.sort(key=lambda x: x.getEvaluation(), reverse=True)
        people_next.extend(family[:2])

    # mutation
    for p in people_next:
        if((random.randint(1, 100) / decimal.Decimal(100)) <= PROBABILITY_MUTATION):
            p.mutate()

    # next generation
    result = evolution(people_next, world, generation+1)

    return result


if __name__ == '__main__':

    print('---------- TEST ----------')
    human1 = Human(10, 2, 0.01)
    human1.generate()
    human2 = Human(10, 2, 0.01)
    human2.generate()
    children12 = human1 * human2
    print('human1   : ', human1.getGeneSequence(), end=' ')
    print('human2   : ', human2.getGeneSequence())
    print('children1: ', children12[0].getGeneSequence(), end=' ')
    print('children2: ', children12[1].getGeneSequence())
    print('---------- TEST ----------')

    world = World()
    print('\r\nA world has been created.')

    people = []
    # create people with random gene sequences
    for i in range(MAX_GENES):
        human = Human(LENGTH_GENE, 2, FREQUENCY_MUTATION)
        human.generate()
        people.append(human)

    print(len(people), 'people enter the world today!')

    result = evolution(people, world, 1) # continue evolution up to MAX_GENERATION

    print('\r\nEvolution has finished.')
    print('The best one is ', result)
