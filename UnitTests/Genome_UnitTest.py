import unittest
import Genome
import GAutils
import Steel

CONST_MAX_THICKNESS = 80
CONST_MAX_WIDTH = 10
CONST_MAX_ZINC_THICKNESS = 80
CONST_MAX_STEEL_GRADE = 10
CONST_MIN_THICKNESS = 20
CONST_MIN_WIDTH = 4
CONST_MIN_ZINC_THICKNESS = 40
CONST_MIN_STEEL_GRADE = 0.1


class TestGenomeClass(unittest.TestCase):
    def test_Genome_sequence(self):
        seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        subject = Genome.Genome(seq)
        self.assertEqual(seq, subject.getSequence())

    def test_Genome_range(self):
        min = 0.2
        max = 0.22
        range = [min, max]
        subject = Genome.Genome()
        subject.setRange(min, max)
        self.assertEqual(range, subject.getRange())
        min = 0.2
        max = 0.22
        self.assertTrue(subject.setRange(min, max))
        min = 0.2
        max = 0.18
        self.assertFalse(subject.setRange(min, max))

    def test_Genome_eval(self):
        coils = GAutils.get_coils_from_excel()
        subject = Genome.Genome()
        subject.evaluate(subject.sequence, Steel.calculate_max_penalty(), coils)
        self.assertTrue(subject.penalty < 1 and subject.penalty > 0)
        self.assertTrue(subject.fitness < 1 and subject.fitness > 0)
        self.assertTrue(subject.fitness + subject.penalty == 1)


if __name__ == '__main__':
    unittest.main()
