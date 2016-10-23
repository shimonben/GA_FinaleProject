import unittest
import GAutils


class TestAll(unittest.TestCase):
    def test_is_improvement_exist(self):
        coils = GAutils.get_coils_from_excel()
        self.assertTrue(GAutils.testing_the_algorithm(coils) > 0)


if __name__ == '__main__':
    unittest.main()
