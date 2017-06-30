import GAutils


def replacement_elitism(population, child1, child2):
    """
    This method search for the lesser good solutions and replace them with the new solutions
    :param population: the population to work with
    :param child1: the firs solution to push
    :param child2: the second solution to push
    :return: the new population
    """
    new_population = population
    pop = population.getPop()
    index = 0
    min = pop[0].getFit()
    for i in range(GAutils.CONST_POPULATION_SIZE):
        if pop[i].getFit() < min:
            min = pop[i].getFit()
            index = i
    pop.pop(index)
    index = 0
    min = pop[0].getFit()
    for i in range(GAutils.CONST_POPULATION_SIZE - 1):
        if pop[i].getFit() < min:
            min = pop[i].getFit()
            index = i
    pop.pop(index)
    pop.append(child1)
    pop.append(child2)
    new_population.setPop(pop)
    return new_population
