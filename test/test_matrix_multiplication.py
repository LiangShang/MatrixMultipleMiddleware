__author__ = 'Sherlock'

from unittest import *
from matrix_multiplication import *


class MatrixMultiplicationTest(TestCase):
    def test_get_matrix_from_json(self):
        json_string = '[1,2,3]'
        self.assertEqual([[1, 2, 3]], get_matrix_from_json(json_string))

        json_string = '1'
        self.assertEqual([[1]], get_matrix_from_json(json_string))

        json_string = '[[1,1,1],[2,2,2],[3,3,3]]'
        self.assertEqual([[1, 1, 1], [2, 2, 2], [3, 3, 3]], get_matrix_from_json(json_string))

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