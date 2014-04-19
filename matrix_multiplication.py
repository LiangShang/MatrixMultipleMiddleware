__author__ = 'Sherlock'
import json


def matrix_multiply(raw_data):
    return None


def multiply(matrix1, matrix2):
    row_num = get_row_length_of(matrix1)
    col_num = get_column_length_of(matrix2)
    result = [[0 for col in range(col_num)] for row in range(row_num)]



    return result


def refine(matrix):
    if type(matrix) == int:
        return [[matrix]]
    elif type(matrix) == list and type(matrix[0]) == int:
        return [matrix]
    else:
        return matrix


def get_row_length_of(matrix):
    return len(matrix[0])


def get_column_length_of(matrix):
    return len(matrix)


def get_matrix_from_json(string):
    raw_matrix = json.loads(string)
    return refine(raw_matrix)