from cpu_multiplier import CPUMultiplier
from utils import HOST, PORT, BUFFER, parse_raw_data

__author__ = 'Sherlock'

import socket
import json


class Server:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def matrix_multiply(self, raw_data):
        result_string = json.dumps(
            self.multiplier.multiply(*parse_raw_data(raw_data)))
        if len(result_string) % BUFFER == 0:
            result_string.append(' ')
        return result_string

    def run(self):
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
            result = self.matrix_multiply(msg_received)
            client_sock.send(result)
        sock.close()

if __name__ == '__main__':
    multiplier = CPUMultiplier()
    Server(multiplier).run()
