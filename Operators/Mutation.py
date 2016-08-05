import GAutils
import random


def mutate(child):
    i = random.randint(0, GAutils.CONST_SEQUENCE_LENGTH)
    j = random.randint(i, GAutils.CONST_SEQUENCE_LENGTH)
    temp = random.uniform(0, 1)
    if temp < GAutils.CONST_MUTATION_PROBABILITY:
        temp_sequence = child.sequence[i:j]
        c = []
        for k in range(len(temp_sequence)):
            c.append(temp_sequence[len(temp_sequence) - k - 1])
        child.sequence[i:j] = c
    return child
