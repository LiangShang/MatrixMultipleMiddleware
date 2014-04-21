import random
import time
import json
from matrix_multiplication import matrix_multiply

__author__ = 'Sherlock'


def generate_matrix_string(row, common, column):
    matrix1 = [[random.randint(0, 101) for c in range(common)]
               for r in range(row)]
    matrix2 = [[random.randint(0, 101) for c in range(column)]
               for r in range(common)]
    return json.dumps(matrix1)+'<|>'+json.dumps(matrix2)

if __name__ == '__main__':
    matrix_string = generate_matrix_string(100, 100, 100)
    start_time = time.time()
    result = matrix_multiply(matrix_string)
    end_time = time.time()

    print 'Time cost is {0} seconds'.format(end_time - start_time)