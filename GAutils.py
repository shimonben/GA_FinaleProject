from openpyxl import load_workbook
from openpyxl import Workbook
import Population
import Steel
from Operators.CrossOver import crossover
from Operators.Mutation import mutate
from Operators.Selection import rouletteSelection
from Operators.Replacement import replacement_elitism
import numpy

CONST_SEQUENCE_LENGTH = 20
CONST_POPULATION_SIZE = 250
CONST_GENERATIONS = 1000
CONST_GENERATIONS_TO_TEST = 1000
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
    temp = []
    for i in range(CONST_GENERATIONS):
        population.updateGenesRange()
        best = population.get_best_solution()
        if i == 0:
            temp.append(population.get_chromosome_by_index(best[0]).getSequence())
            temp.append(best[1])
            lst.append(temp)
            temp = []
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
        if i == (CONST_GENERATIONS - 1):
            temp.append(population.get_chromosome_by_index(best[0]).getSequence())
            temp.append(best[1])
            lst.append(temp)
    save_data_to_excel(lst)


def save_data_to_excel_first_and_last(lst):
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "first generation:"
    ws["C1"] = "last generation:"
    ws["F1"] = "fitness improvement:"
    ws["F2"] = "penalty improvement:"
    ws["G1"] = float(float(lst[1][1])/float(lst[0][1]))*100
    ws["G2"] = float((1-float(lst[1][1])) / (1-float(lst[0][1])))*100
    cell = "A" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = "first generation fit:"
    cell = "C" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = "last generation fit:"
    cell = "B"
    for i in range(2):
        for j in range(CONST_SEQUENCE_LENGTH):
            temp = cell + str(j+1)
            ws[temp] = int(lst[i][0][j])
        cell = "D"
    cell = "B" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = float(lst[0][1])
    cell = "D" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = float(lst[1][1])
    wb.save("1st & last gens.xlsx")


def testing_the_algorithm_1000_runs(coils):
    sum_first_generation_fit = 0
    sum_last_generation_fit = 0
    sum_fit_improvement = 0
    sum_penalty_improvement = 0
    temp_first = 0
    temp_last = 0
    for run in range(CONST_GENERATIONS_TO_TEST):
        population = Population.Population(coils)
        population.createInitial(CONST_POPULATION_SIZE)
        for i in range(CONST_GENERATIONS):
            population.updateGenesRange()
            best = population.get_best_solution()
            if i == 0:
                sum_first_generation_fit += best[1]
                temp_first = best[1]
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
            if i == (CONST_GENERATIONS - 1):
                sum_last_generation_fit += best[1]
                temp_last = best[1]
        sum_fit_improvement += (temp_last/temp_first)*100
        sum_penalty_improvement += ((1-temp_last)/(1-temp_first))*100
        print(run)
    sum_first_generation_fit /= CONST_GENERATIONS_TO_TEST
    sum_last_generation_fit /= CONST_GENERATIONS_TO_TEST
    sum_fit_improvement /= CONST_GENERATIONS_TO_TEST
    sum_penalty_improvement /= CONST_GENERATIONS_TO_TEST
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "first generation avg:"
    ws["B1"] = "last generation avg:"
    ws["C1"] = "fitness improvement avg:"
    ws["D1"] = "penalty improvement avg:"
    ws["E1"] = "population size:"
    ws["A2"] = sum_first_generation_fit
    ws["B2"] = sum_last_generation_fit
    ws["C2"] = sum_fit_improvement
    ws["D2"] = sum_penalty_improvement
    ws["E2"] = CONST_POPULATION_SIZE
    file_name = str(CONST_GENERATIONS_TO_TEST) + " runs avg.xlsx"
    wb.save(file_name)


def save_data_to_excel(lst):
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "sequence to use:"
    ws["C1"] = "fitness improvement:"
    ws["C2"] = "penalty improvement:"
    ws["D1"] = float(float(lst[1][1])/float(lst[0][1]))*100
    ws["D2"] = float((1-float(lst[1][1])) / (1-float(lst[0][1])))*100
    cell = "A" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = "last generation fit:"
    cell = "B"
    for j in range(CONST_SEQUENCE_LENGTH):
        temp = cell + str(j+1)
        ws[temp] = int(lst[1][0][j])
    cell = "B" + str(CONST_SEQUENCE_LENGTH + 1)
    ws[cell] = float(lst[1][1])
    wb.save("output.xlsx")


def testing_the_algorithm_total_and_best_improvement(coils):
    population = Population.Population(coils)
    population.createInitial(CONST_POPULATION_SIZE)
    best_improve = []
    total_improve = []
    for i in range(CONST_GENERATIONS):
        population.updateGenesRange()
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
        best_improve.append(best[1])
        total_improve.append(population.getFitness())
    save_data_to_excel_self_and_total_improve(best_improve, total_improve)


def save_data_to_excel_self_and_total_improve(lst_best, lst_total):
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "best solution improvement:"
    ws["B1"] = "population improvement:"
    cell1 = "A"
    cell2 = "B"
    for j in range(CONST_GENERATIONS):
        ws[cell1 + str(j + 2)] = float(lst_best[j])
        ws[cell2 + str(j + 2)] = float(lst_total[j])
    wb.save("total and best improvements.xlsx")