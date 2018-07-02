# -*- coding: utf-8 -*-
import socket
import json
import sys


def main(query):
    """" Runs the query and prints the results """

    # Criating TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 9001)
    sock.connect(server_address)

    try:
        # Sending query and receiving results
        sock.send(query.encode())

        if query:
            data = sock.recv(512000)
            result = json.loads(data.decode())
            print('Foram encontradas %s ocorrências pelo termo: "%s"' % (len(result), query))
            print('\n'.join(sorted(result)))
        else:
            print('Deve ser informado ao menos um termo de consulta')

    except Exception as ex:
        print(ex)

    finally:
        # Closing the socket
        sock.close()


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print('A query must be issued')
    else:
        main(sys.argv.pop())
