import unittest

__author__ = 'Sherlock'

from cpu_multiplier import *


class MatrixMultiplicationTest(unittest.TestCase):

    def setUp(self):
        self.multiplier = CPUMultiplier()

    def test_get_column_length_of(self):
        matrix = [[1]]
        self.assertEqual(1, self.multiplier.get_column_length_of(matrix))

        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(5, self.multiplier.get_column_length_of(matrix))

        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(3, self.multiplier.get_column_length_of(matrix))

    def test_get_row_length_of(self):
        matrix = [[1]]
        self.assertEqual(1, self.multiplier.get_row_length_of(matrix))

        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(1, self.multiplier.get_row_length_of(matrix))

        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(5, self.multiplier.get_row_length_of(matrix))

        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(3, self.multiplier.get_row_length_of(matrix))

    def test_multiply(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
        self.assertEqual([[90, 96, 102], [216, 231, 246], [342, 366, 390]],
                         self.multiplier.multiply(matrix1, matrix2))

if __name__ == '__main__':
    unittest.main()