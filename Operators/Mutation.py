import GAutils
import random



def mutate(child):
    """
    This method thakes a solution and alter it if the random number is between [0-CONST_MUTATION_PROBABILITY]
    :param child: the solution to work with
    :return: the solution after the mutation
    """
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
