import GAutils
import numpy


class Genome:
    """
    A class that describes the solution
    """

    def __init__(self, seq=0):
        """
        solution initialization
        :param seq: the sequence that builds or needs to be build
        """
        if seq == 0:
            self.sequence = numpy.random.permutation(GAutils.CONST_SEQUENCE_LENGTH)
        else:
            self.sequence = seq
        self.sequence = list(self.sequence)
        self.fitness = 0
        self.range = [0, 0]
        self.penalty = 0

    def getSequence(self):
        """
        This method extract the sequence of a slution
        :return: The solutions' sequence
        """
        return self.sequence

    def setRange(self, minRange, maxRange):
        """
        This method build the range of the pie slice for the roulette selection based on the solutions' fitness
        :param minRange: the minimum range [0,<1]
        :param maxRange: the maximum range [0,1]
        :return: True for success, False otherwise
        """
        if minRange < maxRange:
            self.range = [minRange, maxRange]
            return True
        else:
            return False

    def getRange(self):
        """
        This method extract the solution range
        :return: the solution range
        """
        return self.range

    def getFit(self):
        """
        This method extract the solution fitness
        :return: the solution fitness
        """
        return self.fitness

    def evaluate(self, sequence, max_penalty, coils):
        """
        This method evaluate the whole sequence fitness based on each penalty transition
        :param sequence: the solutions' sequence
        :param max_penalty: the maximum penalty for a transition (used for debug and research)
        :param coils: the coils to examine
        :return: NONE
        """
        penalty = 0
        for i in range(GAutils.CONST_SEQUENCE_LENGTH - 1):
            temp = coils[sequence[i]].calculate_penalty(coils[sequence[i + 1]])
            penalty += temp
        self.fitness = 1 - (penalty / (GAutils.CONST_SEQUENCE_LENGTH - 1))
        self.penalty = penalty / (GAutils.CONST_SEQUENCE_LENGTH - 1)

    def get_penalty(self):
        """
        This method extract the penalty of a sequence
        :return: the penalty
        """
        return self.penalty
