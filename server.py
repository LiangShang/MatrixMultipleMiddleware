__author__ = 'Sherlock'

import socket
from matrix_multiplication import matrix_multiply

HOST = ''
PORT = 50000
BUFFER = 4096

if __name__ == 'main':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(0)
    print "TCP server listens at: {0}:{1}".format(HOST, PORT)

    client_sock, client_addr = sock.accept()
    print "{0}:{1} connect".format(*client_addr)
    while True:
        recv = client_sock.recv(BUFFER)
        if not recv:
            client_sock.close()
            break
        matrix_multiply(recv)
        print "[Client {0}:{1} said]: {2}".format(client_addr[0], client_addr[1], recv)
        client_sock.send('TCP server has received your message')
    sock.close()
