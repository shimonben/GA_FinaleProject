# Genetic Algorithm testing - by Shimon Ben-Alul
import random
import numpy
import Steel
import Genome
import Population

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 50
CONST_MUTATION_PROBABILITY = 0.6


def main():

    #simulate_cross_and_mutate()
    #simulate_ranges_and_roulette()
    #simulate_roulette_selection()
    lst = initialize_the_steel_coils()
    dict = lst[0]
    coils = lst[1]
    for word in dict:
        print(coils[word].print_attr())
    #print("this is just for simulation")


def initialize_the_steel_coils():
    dict = {}
    coils = []
    for i in range(CONST_SEQUENCE_LENGTH):
        thickness = random.uniform(0.1, 50)
        width = random.uniform(0.1, 50)
        zinc_thickness = random.uniform(0.1, 3)
        steel_grade = random.randint(0, 10)
        dict[i] = "Steel #{}".format(i)
        temp = Steel.Steel(thickness, width, zinc_thickness, steel_grade, i)
        coils.append(temp)
    lst = [dict, coils]
    return lst


def simulate_roulette_selection():
    population = Population.Population()
    population.createInitial(CONST_POPULATION_SIZE)
    population.updateGenesRange()
    selected = population.rouletteSelection()
    for select in selected:
        print(select.getSequence())


def simulate_ranges_and_roulette():
    population = Population.Population()
    population.createInitial(CONST_POPULATION_SIZE)
    population.updateGenesRange()
    genes = population.getPop()
    for gene in genes:
        print(gene.getRange())


def simulate_cross_and_mutate():
    population = Population.Population()
    population.createInitial(CONST_POPULATION_SIZE)
    genes = population.getPop()
    gene1 = genes[5]
    gene2 = genes[8]
    crossOverPoint = random.randint(0, CONST_SEQUENCE_LENGTH)
    offspring = gene1.crossover(gene2, crossOverPoint)
    print("The selected parents:")
    print(gene1.getSequence())
    print(gene2.getSequence())
    print("The crossover is being started at: ", crossOverPoint)
    print("Their Children:")
    for kid in offspring:
        print(kid.getSequence())
    print("The offspring mutation probability is: ", CONST_MUTATION_PROBABILITY)
    print("The offspring after mutation:")
    c1 = offspring[0]
    c2 = offspring[1]
    c1.mutate(CONST_MUTATION_PROBABILITY)
    c2.mutate(CONST_MUTATION_PROBABILITY)
    print(c1.getSequence())
    print(c2.getSequence())


if __name__ == "__main__": main()

