import unittest
import Steel
import GAutils
import Population


class TestSteelClass(unittest.TestCase):
    def test_calculate_max_penalty(self):
        # we calculated the max penalty outside the program: 29.18
        self.assertEqual(29.18, Steel.calculate_max_penalty())

    def test_calculate_transition_penalty(self):
        # we calculated the transition penalty between the 2 first coils outside the program: 0.1885
        coils = GAutils.get_coils_from_excel()
        population = Population.Population(coils)
        population.createInitial(GAutils.CONST_POPULATION_SIZE)
        # coils[0] is pf type Steel and holds the attributes for the coils
        temp = coils[0].calculate_penalty(coils[1])
        temp = float("%.4f" % temp)
        self.assertAlmostEqual(temp, 0.1984)


if __name__ == '__main__':
    unittest.main()
