import GAutils
import numpy


class Genome:
    def __init__(self, seq=0):
        if seq == 0:
            self.sequence = numpy.random.permutation(GAutils.CONST_SEQUENCE_LENGTH)
        else:
            self.sequence = seq
        self.sequence = list(self.sequence)
        self.fitness = 0
        self.range = [0, 0]
        self.penalty = 0

    def getSequence(self):
        return self.sequence

    def setRange(self, minRange, maxRange):
        if minRange < maxRange:
            self.range = [minRange, maxRange]
            return True
        else:
            return False

    def getRange(self):
        return self.range

    def getFit(self):
        return self.fitness

    def evaluate(self, sequence, max_penalty, coils):
        penalty = 0
        for i in range(GAutils.CONST_SEQUENCE_LENGTH - 1):
            temp = coils[sequence[i]].calculate_penalty(coils[sequence[i+1]])
            temp = temp / max_penalty
            penalty += temp
        self.fitness = 1 - (penalty / (GAutils.CONST_SEQUENCE_LENGTH - 1))
        self.penalty = penalty / (GAutils.CONST_SEQUENCE_LENGTH - 1)

    def get_penalty(self):
        return self.penalty
