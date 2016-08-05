from openpyxl import load_workbook
import Population
import Steel
from Operators.CrossOver import crossover
from Operators.Mutation import mutate
from Operators.Selection import rouletteSelection
from Operators.Replacement import replacement_elitism

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 500
CONST_GENERATIONS = 5000
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
            coils.append(temp)
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
        pop = population.getPop()
        selected = rouletteSelection(population)
        offspring = crossover(selected[0], selected[1])
        c1 = offspring[0]
        c2 = offspring[1]
        c1 = mutate(c1)
        c2 = mutate(c2)
        c1.evaluate(c1.getSequence(), Steel.calculate_max_penalty(), population.coils)
        c2.evaluate(c2.getSequence(), Steel.calculate_max_penalty(), population.coils)
        population = replacement_elitism(population, offspring[0], offspring[1])
        population.update_fitness()
        best = population.get_best_solution()
        print("Generation ", i, " best: ", population.get_chromosome_by_index(best[0]).getSequence(), ", with fitness: ", best[1])
        lst.append(best)
    return lst
