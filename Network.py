#reusable!

import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ONLINE SERVER:
        # 45.56.108.66
        # LOCAL SERVER FOR DEBUGGING:
        # 128.226.250.52
        self.server = "128.226.250.52"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    # get player
    def getData(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # gets player from server at connection and then returns this unloaded player as self.p which can be accessed by client (client's own information)
            return pickle.loads(self.client.recv(4096))
        except:
            pass

    def send(self, data):
        try:
            # sends loaded object to server
            self.client.send(pickle.dumps(data))
            # loads data with pickle and returns it for use in client
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)