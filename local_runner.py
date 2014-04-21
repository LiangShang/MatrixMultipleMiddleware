
import time

from matrix_multiplication import matrix_multiply
from utils import generate_matrix_string

__author__ = 'Sherlock'


if __name__ == '__main__':
    matrix_string = generate_matrix_string(100, 100, 100)
    start_time = time.time()
    result = matrix_multiply(matrix_string)
    end_time = time.time()

    print 'Time cost is {0} seconds'.format(end_time - start_time)