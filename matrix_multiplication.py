__author__ = 'Sherlock'
import json


def matrix_multiply(raw_data):
    return multiply(*parse_raw_data(raw_data))


def multiply(matrix1, matrix2):

    row_num = get_row_length_of(matrix1)
    col_num = get_column_length_of(matrix2)
    result = [[0 for col in range(col_num)] for row in range(row_num)]

    for row in range(row_num):
        for col in range(col_num):
            result[row][col] = \
                sum([matrix1[row][i]*matrix2[i][col]
                     for i in range(get_row_length_of(matrix2))])

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


def parse_raw_data(raw_data):
    return tuple(map(get_matrix_from_json, raw_data.split('<|>')))


def get_matrix_from_json(string):
    raw_matrix = json.loads(string)
    return refine(raw_matrix)