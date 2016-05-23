# Genetic Algorithm testing - by Shimon Ben-Alul
import random
import numpy
import Steel
import Genome
import Population
import csv

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 50
CONST_MUTATION_PROBABILITY = 0.7
CONST_MAX_THICKNESS = 50
CONST_MAX_WIDTH = 50
CONST_MAX_ZINC_THICKNESS = 5
CONST_MAX_STEEL_GRADE = 10
CONST_MIN_THICKNESS = 0.1
CONST_MIN_WIDTH = 0.1
CONST_MIN_ZINC_THICKNESS = 0.1
CONST_MIN_STEEL_GRADE = 0.1
CONST_GENERATIONS = 500


# TODO dont forget to change the weights in Steel calss
def main():
    writer = []
    for t in range(100):
        coils = initialize_the_steel_coils()
        population = Population.Population(coils)
        population.createInitial(CONST_POPULATION_SIZE)
        for i in range(CONST_GENERATIONS):
            if i == 0:
                total_fit = population.getFitness()
                best = population.get_best_solution()
                temp = [total_fit, best[1]]
            population.updateGenesRange()
            selected = population.rouletteSelection()
            offspring = selected[0].crossover(selected[1])
            c1 = offspring[0]
            c2 = offspring[1]
            c1.mutate(CONST_MUTATION_PROBABILITY)
            c2.mutate(CONST_MUTATION_PROBABILITY)
            c1.evaluate(c1.getSequence(), Steel.calculate_max_penalty(), population.coils)
            c2.evaluate(c2.getSequence(), Steel.calculate_max_penalty(), population.coils)
            # population.replacement_both_parents(selected[0], selected[1], offspring[0], offspring[1])
            population.replacement_random(offspring[0], offspring[1])
            # population.replacement_elitism(offspring[0], offspring[1])
            population.update_fitness()
            best = population.get_best_solution()
            total_fit = population.getFitness()
            # temp = "Generation: {:0>-3}, Total fit: {:07.4f}, {:0>-2} is the best Fit: {:07.4f}".format(i, total_fit, best[0], best[1])
            # print(temp)
        total_fit = population.getFitness()
        best = population.get_best_solution()
        total_dif = total_fit - temp[0]
        best_dif = best[1] - temp[1]
        temp = [total_dif, best_dif]
        writer.append(temp)
    write_to_file(writer, 'test')


def initialize_the_steel_coils():
    dict = {}
    coils = []
    for i in range(CONST_SEQUENCE_LENGTH):
        thickness = random.uniform(CONST_MIN_THICKNESS, CONST_MAX_THICKNESS)
        width = random.uniform(CONST_MIN_WIDTH, CONST_MAX_WIDTH)
        zinc_thickness = random.uniform(CONST_MIN_ZINC_THICKNESS, CONST_MAX_ZINC_THICKNESS)
        steel_grade = random.uniform(CONST_MIN_STEEL_GRADE, CONST_MAX_STEEL_GRADE)
        temp = Steel.Steel(thickness, width, zinc_thickness, steel_grade, i)
        dict[i] = temp.print_attr()
        coils.append(temp)
    return coils

def write_to_file(lst, file_name):
    with open('%s.csv' % file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in lst:
            spamwriter.writerow(['%s' % item[0], '%s' % item[1]])



if __name__ == "__main__": main()
