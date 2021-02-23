import socket
import sys


class Server:
    def __init__(self):
        self.__port = 9192
        self.__host = 'localhost'
        self.__server_address = (self.__host, self.__port)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(self.__server_address)
        server.listen()

        connection_one, one_address = server.accept()
        connection_one.send("Waiting for another connection.".encode())
        connection_two, two_address = server.accept()
        connection_one.send(b'1')
        one_pk = connection_one.recv(1024)
        connection_two.send(one_pk)
        two_pk = connection_two.recv(1024)
        connection_one.send(two_pk)




