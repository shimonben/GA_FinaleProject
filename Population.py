import random
import Genome
import main


class Population:
    pop_size = 0
    fitness = 0

    def __init__(self):
        Population.pop_size = 0
        Population.fitness = 0
        self.pop = []
        self.fitnessProbs = 0

    def createInitial(self, size):
        for i in range(size):
            self.pop_size += 1
            a = Genome.Genome()
            a.evaluate()
            self.pop.append(a)
            self.fitness += a.fitness

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
            max += gene.getFit() / totalFit
            gene.setRange(min, max)
            min =  max
        self.fitnessProbs = min

    def getFitnessProb(self):
        return self.fitnessProbs

    def rouletteSelection(self):
        chosen = []
        genes = self.getPop()
        count = 0
        while(count < 2):
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


    #def replacement(self, child1, child2):



