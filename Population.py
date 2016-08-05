import random
import Genome
import GAutils
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
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if i == index:
                return pop[i]

    def getFitness(self):
        return self.fitness

    def getPop(self):
        return self.pop

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

    def setPop(self, pop):
        self.pop = pop

    def get_best_solution(self):
        index = 0
        max = 0
        pop = self.pop
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max:
                max = pop[i].getFit()
                index = i
        lst = [index, max]
        return lst
