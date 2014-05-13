
import time
from socket_server import matrix_multiply

from utils import generate_matrix_string, MATRIX_DEFAULT_SIZE

__author__ = 'Sherlock'


if __name__ == '__main__':
    matrix_string = generate_matrix_string(
        MATRIX_DEFAULT_SIZE,
        MATRIX_DEFAULT_SIZE,
        MATRIX_DEFAULT_SIZE)
    start_time = time.time()
    result = matrix_multiply(matrix_string)
    end_time = time.time()

    print 'Time cost is {0} seconds'.format(end_time - start_time)