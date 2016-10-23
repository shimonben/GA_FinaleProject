import unittest
import Population
import GAutils


class TestPopulationClass(unittest.TestCase):
    def test_get_chromosome_by_index(self):
        coils = GAutils.get_coils_from_excel()
        population = Population.Population(coils)
        population.createInitial(GAutils.CONST_POPULATION_SIZE)
        pop = population.getPop()
        self.assertEqual(pop[1].getSequence(), (population.get_chromosome_by_index(1)).getSequence())
        self.assertNotEqual(pop[1].getSequence(), (population.get_chromosome_by_index(2)).getSequence())

    def test_fitness_prob(self):
        coils = GAutils.get_coils_from_excel()
        population = Population.Population(coils)
        population.createInitial(GAutils.CONST_POPULATION_SIZE)
        population.updateGenesRange()
        self.assertAlmostEqual(population.getFitnessProb(), 1)

    def test_set_get_pop(self):
        coils = GAutils.get_coils_from_excel()
        population1 = Population.Population(coils)
        population1.createInitial(GAutils.CONST_POPULATION_SIZE)
        pop1 = population1.getPop()
        population2 = Population.Population(coils)
        population2.createInitial(GAutils.CONST_POPULATION_SIZE)
        pop2 = population2.getPop()
        self.assertNotEqual(pop1, pop2)
        population2.setPop(pop1)
        pop2 = population2.getPop()
        self.assertEqual(pop1, pop2)

    def test_get_best_sol(self):
        coils = GAutils.get_coils_from_excel()
        population = Population.Population(coils)
        population.createInitial(GAutils.CONST_POPULATION_SIZE)
        pop = population.getPop()
        max_fit = pop[0].getFit()
        index = 0
        for i in range(GAutils.CONST_POPULATION_SIZE):
            if pop[i].getFit() > max_fit:
                index = i
                max_fit = pop[i].getFit()
        self.assertEqual(index, (population.get_best_solution())[0])

if __name__ == '__main__':
    unittest.main()
