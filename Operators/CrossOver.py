import random

import GAutils

from GeneticAlgorithm import Genome


def crossover(chrom1, chrom2):
    position = random.randint(0, GAutils.CONST_SEQUENCE_LENGTH)
    parent1 = chrom1.getSequence()
    parent2 = chrom2.getSequence()
    child1 = parent1[0:position]
    child2 = parent2[0:position]
    parent1 = list(parent1)
    parent2 = list(parent2)
    child1 = list(child1)
    child2 = list(child2)
    for j in range(GAutils.CONST_SEQUENCE_LENGTH):
        if parent2[j] not in child1:
            child1.append(parent2[j])
        if parent1[j] not in child2:
            child2.append(parent1[j])
    c1 = Genome.Genome(child1)
    c2 = Genome.Genome(child2)
    offspring = [c1, c2]
    return offspring
