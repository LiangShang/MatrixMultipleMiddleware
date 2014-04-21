__author__ = 'Sherlock'
import json
import random


HOST = '127.0.0.1'
PORT = 50090
BUFFER = 4096

MATRIX_DEFAULT_SIZE = 100

SPLITTER = '<|>'


def generate_matrix_string(row, common, column):
    matrix1 = [[random.randint(0, 101) for c in range(common)]
               for r in range(row)]
    matrix2 = [[random.randint(0, 101) for c in range(column)]
               for r in range(common)]
    result_string = json.dumps(matrix1)+SPLITTER+json.dumps(matrix2)
    if len(result_string)% BUFFER == 0:
        result_string += ' '
    return result_string


def parse_raw_data(raw_data):
    return tuple(map(get_matrix_from_json, raw_data.split('<|>')))


def get_matrix_from_json(string):
    raw_matrix = json.loads(string)
    return refine(raw_matrix)


def refine(matrix):
    if type(matrix) == int:
        return [[matrix]]
    elif type(matrix) == list and type(matrix[0]) == int:
        return [matrix]
    else:
        return matrix
