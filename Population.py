import random
import Genome
import GAutils
import Steel


class Population:
    """
    Class to describe the population
    """
    pop_size = 0
    fitness = 0

    def __init__(self, coils):
        """
        initialize the empty population
        :param coils: the coil to initialize the population with
        """
        Population.pop_size = 0
        Population.fitness = 0
        self.pop = []
        self.fitnessProbs = 0
        self.coils = coils

    def createInitial(self, size):
        """
        This method builds the population
        :param size: the size of the population
        :return: NONE
        """
        self.pop_size = size
        for i in range(size):
            a = Genome.Genome()
            a.evaluate(a.getSequence(), Steel.calculate_max_penalty(), self.coils)
            self.pop.append(a)
            self.fitness += a.fitness

    def update_fitness(self):
        """
        update the fitness of each chromosome in the population
        :return: NONE
        """
        self.fitness = 0
        pop = self.pop
        for chromosome in pop:
            self.fitness += chromosome.fitness

    def get_chromosome_by_index(self, index):
        """
        This method returns a requested solution from the population
        :param index: the requested index
        :return: the requested solution
        """
        pop = self.getPop()
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if i == index:
                return pop[i]

    def getFitness(self):
        """
        This method returns the population Fitness
        :return: population fit
        """
        return self.fitness

    def getPop(self):
        """
        This method returns the population
        :return: the population
        """
        return self.pop

    def updateGenesRange(self):
        """
        This method updates the solution ranges for the roulette selection
        :return: NONE
        """
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
        """
        This method returns fitness probability
        :return: fitness probability
        """
        return self.fitnessProbs

    def setPop(self, pop):
        """
        This method sets the population
        :param pop:
        :return: NONE
        """
        self.pop = pop

    def get_best_solution(self):
        """
        This method checks the best solution in the population
        :return: The best solution
        """
        index = 0
        max = 0
        pop = self.pop
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max:
                max = pop[i].getFit()
                index = i
        lst = [index, max]
        return lst
