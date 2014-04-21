from utils import HOST, PORT, BUFFER, parse_raw_data

__author__ = 'Sherlock'

import socket
from matrix_multiplication import multiply
import json


def matrix_multiply(raw_data):
    result_string = json.dumps(multiply(*parse_raw_data(raw_data)))
    if len(result_string) % BUFFER == 0:
        result_string += ' '
    return result_string

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(0)
    print "TCP server listens at: {0}:{1}".format(HOST, PORT)

    client_sock, client_addr = sock.accept()
    print "{0}:{1} connect".format(*client_addr)
    while True:
        msg_received = ''
        while True:
            recv = client_sock.recv(BUFFER)
            msg_received += recv
            if len(recv) < BUFFER:
                break
        result = matrix_multiply(msg_received)
        client_sock.send(result)
    sock.close()
