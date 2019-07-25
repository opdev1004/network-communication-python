import socket
import sys

class Client:
    def __init__(self):
        self.client  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Server IP address and port
        self.server = "192.168.1.14"
        self.port = 5555
        self.addr = (self.server, self.port)

    # if server does not exists, it stucks for waiting
    def send(self, data):
        try:
            self.client.sendto(str.encode(data), (self.server, self.port))
            receivedData, addr = self.client.recvfrom(2048)
            return receivedData.decode("utf-8")
        except socket.error as e:
            print(e)

c = Client()
print(c.send("sss"))
print(c.send("aaa"))
