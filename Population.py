import random
import Genome
import main
import Steel


class Population:
    pop_size = 0
    fitness = 0

    def __init__(self, coils):
        Population.pop_size = 0
        Population.fitness = 0
        self.pop = []
        self.fitnessProbs = 0
        self.coils = coils

    def createInitial(self, size):
        self.pop_size = size
        for i in range(size):
            a = Genome.Genome()
            a.evaluate(a.getSequence(), Steel.calculate_max_penalty(), self.coils)
            self.pop.append(a)
            self.fitness += a.fitness

    def update_fitness(self):
        self.fitness = 0
        pop = self.pop
        for chromosome in pop:
            self.fitness += chromosome.fitness

    def get_chromosome_by_index(self, index):
        pop = self.getPop()
        for i in range(main.CONST_POPULATION_SIZE):
            if i == index:
                return pop[i]

    def getFitness(self):
        return self.fitness

    def getPop(self):
        return self.pop

    def createOffspring(self, parent1, parent2):
        crossOverPoint = random.randint(0, main.CONST_SEQUENCE_LENGTH)
        offspring = parent1.crossover(parent2, crossOverPoint)
        c1 = offspring[0]
        c2 = offspring[1]
        c1.mutate(main.CONST_MUTATION_PROBABILITY)
        c2.mutate(main.CONST_MUTATION_PROBABILITY)
        return offspring

    def updateGenesRange(self):
        genes = self.getPop()
        totalFit = self.fitness
        min = 0
        max = 0
        for gene in genes:
            max += (gene.getFit() / totalFit)
            gene.setRange(min, max)
            min = max
        self.fitnessProbs = min

    def getFitnessProb(self):
        return self.fitnessProbs

    def rouletteSelection(self):
        chosen = []
        genes = self.getPop()
        count = 0
        while (count < 2):
            temp = random.uniform(0, self.getFitnessProb())
            for gene in genes:
                range = gene.getRange()
                max = range[1]
                min = range[0]
                if temp < max and temp > min:
                    if count == 0:
                        chosen.append(gene)
                        count += 1
                    else:
                        if chosen[0] != gene:
                            chosen.append(gene)
                            count += 1
        return chosen

    def replacement_both_parents(self, parents1, parent2, child1, child2):
        pops = self.getPop()
        index1 = pops.index(parents1)
        index2 = pops.index(parent2)
        pops.pop(index1)
        if index2 == main.CONST_POPULATION_SIZE - 1:
            index2 -= 1
        pops.pop(index2)
        pops.append(child1)
        pops.append(child2)

    def replacement_random(self, child1, child2):
        pops = self.getPop()
        index1 = random.randint(0, main.CONST_POPULATION_SIZE - 1)
        pops.pop(index1)
        index2 = random.randint(0, main.CONST_POPULATION_SIZE - 2)
        pops.pop(index2)
        pops.append(child1)
        pops.append(child2)

    def replacement_elitism(self, child1, child2):
        pop = self.getPop()
        index = 0
        min = pop[0].getFit()
        for i in range(main.CONST_POPULATION_SIZE):
            if pop[i].getFit() < min:
                min = pop[i].getFit()
                index = i
        pop.pop(index)
        index = 0
        min = pop[0].getFit()
        for i in range(main.CONST_POPULATION_SIZE - 1):
            if pop[i].getFit() < min:
                min = pop[i].getFit()
                index = i
        pop.pop(index)
        pop.append(child1)
        pop.append(child2)

    def get_best_solution(self):
        index = 0
        max = 0
        pop = self.pop
        for i in range(main.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max:
                max = pop[i].getFit()
                index = i
        lst = [index, max]
        return lst
