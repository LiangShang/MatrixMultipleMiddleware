
__author__ = 'Sherlock'

from unittest import *
from matrix_multiplication import *


class MatrixMultiplicationTest(TestCase):

    def test_get_column_length_of(self):
        matrix = [[1]]
        self.assertEqual(1, get_column_length_of(matrix))

        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(5, get_column_length_of(matrix))

        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(3, get_column_length_of(matrix))

    def test_get_row_length_of(self):
        matrix = [[1]]
        self.assertEqual(1, get_row_length_of(matrix))

        matrix = [[1], [2], [3], [4], [5]]
        self.assertEqual(1, get_row_length_of(matrix))

        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(5, get_row_length_of(matrix))

        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(3, get_row_length_of(matrix))

    def test_multiply(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
        self.assertEqual([[90, 96, 102], [216, 231, 246], [342, 366, 390]],
                         multiply(matrix1, matrix2))

