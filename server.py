# -*- coding: utf-8 -*-
from engine import load_files, query
import socket
import json

def run(port=9001):
    try:
        # Carregando índice
        load_files()

        # Criando socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Criando socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', port)
        print('Starting server at %s:%s' % server_address)
        sock.bind(server_address)

        # Setting socket to listen mode
        sock.listen(1)

        while True:
            # Waiting for conections
            print('Waiting for connections...')
            connection, client_address = sock.accept()

            try:
                # Handlind socket request and returning search result
                while True:
                    # Receives queries up to 2KB
                    data = connection.recv(2048)
                    print('Request received: "%s"' % data.decode())
                    if data:
                        response = json.dumps(query(data.decode()))

                        # Sending response back to the client
                        connection.send(response.encode())

                        break
                    else:
                        print('Query was empty.')
                        break

            finally:
                # Clean up the connection
                connection.close()
    except KeyboardInterrupt:
        print('Shutting down server...')
        exit(0)

if __name__ == "__main__":
    run()