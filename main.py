# Genetic Algorithm testing - by Shimon Ben-Alul
import pickle
import random

import Steel
import Population
import csv

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 200
CONST_GENERATIONS = 100000000

CONST_MUTATION_PROBABILITY = 0.75
CONST_MAX_THICKNESS = 80
CONST_MAX_WIDTH = 10
CONST_MAX_ZINC_THICKNESS = 80
CONST_MAX_STEEL_GRADE = 10
CONST_MIN_THICKNESS = 20
CONST_MIN_WIDTH = 4
CONST_MIN_ZINC_THICKNESS = 40
CONST_MIN_STEEL_GRADE = 0.1


def main():
    coils_are_already_saved = 1
    if coils_are_already_saved == 0:
        coils = initialize_the_steel_coils()
        with open('coils.pickle', 'wb') as f:
            pickle.dump(coils, f)
    else:
        with open('coils.pickle', 'rb') as f:
            coils = pickle.load(f)
    testing_the_algorithm(coils)


def testing_the_algorithm(coils):
    population = Population.Population(coils)
    population.createInitial(CONST_POPULATION_SIZE)
    lst = []
    for i in range(CONST_GENERATIONS):
        population.updateGenesRange()
        selected = population.rouletteSelection()
        offspring = selected[0].crossover(selected[1])
        c1 = offspring[0]
        c2 = offspring[1]
        c1.mutate(CONST_MUTATION_PROBABILITY)
        c2.mutate(CONST_MUTATION_PROBABILITY)
        c1.evaluate(c1.getSequence(), Steel.calculate_max_penalty(), population.coils)
        c2.evaluate(c2.getSequence(), Steel.calculate_max_penalty(), population.coils)
        population.replacement_elitism(offspring[0], offspring[1])
        population.update_fitness()
        best = population.get_best_solution()
        total_fit = population.getFitness()
        if i == 0 or i == CONST_GENERATIONS - 1:
            lst.append(best[1])
    print(lst[1] - lst[0])


def preview_the_range_for_the_roulette():
    coils = initialize_the_steel_coils()
    population = Population.Population(coils)
    population.createInitial(CONST_POPULATION_SIZE)
    population.updateGenesRange()
    genes = population.getPop()
    i = 0
    lst = []
    for gene in genes:
        print("gene {:0>2}: from {:7.6f} to {:7.6f}, p({})={:7.6f}".format(i, gene.range[0], gene.range[1], i,
                                                                           gene.range[1] - gene.range[0]))
        temp = []
        temp.append(gene.range[0])
        temp.append(gene.range[1])
        lst.append(temp)
        i += 1
    return lst


def initialize_the_steel_coils():
    coils = []
    for i in range(CONST_SEQUENCE_LENGTH):
        thickness = random.uniform(CONST_MIN_THICKNESS, CONST_MAX_THICKNESS)
        width = random.uniform(CONST_MIN_WIDTH, CONST_MAX_WIDTH)
        zinc_thickness = random.uniform(CONST_MIN_ZINC_THICKNESS, CONST_MAX_ZINC_THICKNESS)
        steel_grade = random.uniform(CONST_MIN_STEEL_GRADE, CONST_MAX_STEEL_GRADE)
        temp = Steel.Steel(thickness, width, zinc_thickness, steel_grade, i)
        coils.append(temp)
    return coils


def create_compareable_csv(filename, replacements_identifier, x=3):
    writer = []
    for t in range(1000):
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
            if replacements_identifier == 0:  # Random Replacement
                population.replacement_random(offspring[0], offspring[1])
            elif replacements_identifier == 1:  # Elitism Replacement
                population.replacement_elitism(offspring[0], offspring[1])
            elif replacements_identifier == 2:  # Both Parents Replacement
                population.replacement_both_parents(selected[0], selected[1], offspring[0], offspring[1])
            elif replacements_identifier == 3:  # Every x generation
                if i % x == 0:
                    population.replacement_random(offspring[0], offspring[1])
                else:
                    population.replacement_elitism(offspring[0], offspring[1])
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
    write_to_file(writer, filename)


def write_to_file(lst, file_name):
    with open('%s.csv' % file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in lst:
            spamwriter.writerow(['%s' % item[0], '%s' % item[1]])


if __name__ == "__main__": main()
