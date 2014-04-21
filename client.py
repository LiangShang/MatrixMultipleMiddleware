import time
from utils import generate_matrix_string, MATRIX_DEFAULT_SIZE

__author__ = 'Sherlock'

import socket
from utils import HOST, PORT, BUFFER


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    send_string = generate_matrix_string(
        MATRIX_DEFAULT_SIZE,
        MATRIX_DEFAULT_SIZE,
        MATRIX_DEFAULT_SIZE)
    start_time = time.time()
    sock.send(send_string)
    msg_received = ''
    while True:
        recv = sock.recv(BUFFER)
        msg_received += recv
        if len(recv) < BUFFER:
            break
    end_time = time.time()
    print '[tcpServer said]: {0}'.format(msg_received)
    print '[time cost is]: {0} seconds'.format(end_time - start_time)
    sock.close()