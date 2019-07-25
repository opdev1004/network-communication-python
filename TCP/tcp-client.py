import socket
from _thread import *
import sys

class Client:
    def __init__(self):
        self.client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Server IP address and port
        self.server = "192.168.1.14"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

c = Client()
print(c.send("sss"))
print(c.send("aaa"))
