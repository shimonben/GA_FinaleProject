import main
import random
import numpy
import Steel


class Genome:
    def __init__(self, seq=0):
        if seq == 0:
            self.sequence = numpy.random.permutation(main.CONST_SEQUENCE_LENGTH)
        else:
            self.sequence = seq
        self.sequence = list(self.sequence)
        self.fitness = 0
        self.range = [0, 0]

    def getSequence(self):
        return self.sequence

    def setRange(self, minRange, maxRange):
        self.range = [minRange, maxRange]

    def getRange(self):
        return self.range

    def getFit(self):
        return self.fitness

    def mutate(self, prob):
        i = random.randint(0, main.CONST_SEQUENCE_LENGTH)
        j = random.randint(i, main.CONST_SEQUENCE_LENGTH)
        temp = random.uniform(0, 1)
        if temp < prob:
            tempSeq = self.sequence[i:j]
            c = []
            for k in range(len(tempSeq)):
                c.append(tempSeq[len(tempSeq) - k - 1])
            self.sequence[i:j] = c

    def evaluate(self, sequence, max_penalty, coils):
        penalty = 0
        for i in range(main.CONST_SEQUENCE_LENGTH):
            if i < (main.CONST_SEQUENCE_LENGTH - 1):
                temp = coils[sequence[i]].calculate_penalty(coils[sequence[i+1]])
                temp = temp / max_penalty
                penalty += temp
        self.fitness = 1 - (penalty / max_penalty)



    def crossover(self, otherChrom):
        position = random.randint(0, main.CONST_SEQUENCE_LENGTH)
        parent1 = self.getSequence()
        parent2 = otherChrom.getSequence()
        child1 = parent1[0:position]
        child2 = parent2[0:position]
        parent1 = list(parent1)
        parent2 = list(parent2)
        child1 = list(child1)
        child2 = list(child2)
        for j in range(main.CONST_SEQUENCE_LENGTH):
            if parent2[j] not in child1:
                child1.append(parent2[j])
            if parent1[j] not in child2:
                child2.append(parent1[j])
        c1 = Genome(child1)
        c2 = Genome(child2)
        offspring = [c1, c2]
        return offspring
