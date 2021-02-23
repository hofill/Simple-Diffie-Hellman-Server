import pyDH
import socket


class Client:
    def __init__(self, host):
        self.__port = 9192
        self.__host = host
        self.__server_address = (self.__host, self.__port)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(self.__server_address)
        pk_two = server.recv(1024)
        if pk_two == b'Waiting for another connection.':
            print("Waiting for another connection")
            pk_two = server.recv(1024)
        dh = pyDH.DiffieHellman()
        server.send(str(dh.gen_public_key()).encode())
        if pk_two == b'1':
            pk_two = server.recv(1024)
        key = dh.gen_shared_key(int(pk_two, 10))
        print(key.encode())
