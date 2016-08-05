import pickle
import Steel
import Population
import csv
from openpyxl import load_workbook

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 500
CONST_GENERATIONS = 1000
CONST_MUTATION_PROBABILITY = 0.75
CONST_MAX_THICKNESS = 80
CONST_MAX_WIDTH = 10
CONST_MAX_ZINC_THICKNESS = 80
CONST_MAX_STEEL_GRADE = 10
CONST_MIN_THICKNESS = 20
CONST_MIN_WIDTH = 4
CONST_MIN_ZINC_THICKNESS = 40
CONST_MIN_STEEL_GRADE = 0.1


def get_coils_from_excel():
    wb = load_workbook('coils.xlsx')
    ws = wb.active
    coils = []
    i = 0
    temp = 'B2:E'
    temp += str(CONST_SEQUENCE_LENGTH + 1)
    for row in ws.iter_rows(temp):
        if check_validity(row, i):
            thickness = row[3].value
            width = row[2].value
            zinc_thickness = row[1].value
            steel_grade = row[0].value
            temp = Steel.Steel(thickness, width, zinc_thickness, steel_grade, i)
            i += 1
        else:
            print("Values are not in range! program shut down")
            exit()
    return coils


def check_validity(row, i):
    if (row[3].value < CONST_MIN_THICKNESS) or (row[3].value > CONST_MAX_THICKNESS):
        print("in coil ", i+1, ", there is a problem with thickness")
        return False
    if (row[2].value < CONST_MIN_WIDTH) or (row[2].value > CONST_MAX_WIDTH):
        print("in coil ", i+1, ", there is a problem with width")
        return False
    if (row[1].value < CONST_MIN_ZINC_THICKNESS) or (row[1].value > CONST_MAX_ZINC_THICKNESS):
        print("in coil ", i+1, ", there is a problem with zinc thickness")
        return False
    if (row[0].value < CONST_MIN_STEEL_GRADE) or (row[0].value > CONST_MAX_STEEL_GRADE):
        print("in coil ", i+1, ", there is a problem with steel grade")
        return False
    return True


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
        print("Generation ", i, " best: ", population.get_chromosome_by_index(best[0]).getSequence(), ", with fitness: ", best[1])
        lst.append(best)
    return lst

def preview_the_range_for_the_roulette(coils):
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


def use_pickle_binary_file():
    with open('coils.pickle', 'rb') as f:
        coils = pickle.load(f)
    preview_the_range_for_the_roulette(coils)
    testing_the_algorithm(coils)


def create_comparable_csv(coils, filename, replacements_identifier, x=3):
    writer = []
    for t in range(1000):
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
    with open('%s.csv' % file_name, 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in lst:
            spam_writer.writerow(['%s' % item[0], '%s' % item[1]])