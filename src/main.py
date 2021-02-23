import sys

from client import Client
from server import Server

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "server":
            server = Server()
            server.start()
        elif sys.argv[1] == "client":
            client = Client(sys.argv[2])
            client.start()
    else:
        print("Argument needed!\n Arguments: server/client")
