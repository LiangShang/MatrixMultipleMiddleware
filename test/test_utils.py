from utils import get_matrix_from_json, parse_raw_data

__author__ = 'Sherlock'


from unittest import *


class UtilsTest(TestCase):

    def test_get_matrix_from_json(self):
        json_string = '[1,2,3]'
        self.assertEqual([[1, 2, 3]], get_matrix_from_json(json_string))

        json_string = '1'
        self.assertEqual([[1]], get_matrix_from_json(json_string))

        json_string = '[[1,1,1],[2,2,2],[3,3,3]]'
        self.assertEqual([[1, 1, 1], [2, 2, 2], [3, 3, 3]], get_matrix_from_json(json_string))

    def test_parse_raw_data(self):
        self.assertEqual(([[1]], [[1]]), parse_raw_data('1<|>1'))

        self.assertEqual(([[1, 2, 3]], [[4, 5, 6], [7, 8, 9]]),
                         parse_raw_data('[1,2,3]<|>[[4,5,6],[7,8,9]]'))