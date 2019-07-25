import socket
import sys

# Server IP address and port
server = "192.168.1.14"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((server, port))

reply = ""

# This does not stop. So it needs a trigger to stop the server.
while True:
    data, addr = s.recvfrom(2048)
    reply = data.decode("utf-8")
    print("SERVER Received: ", reply)
    print("SERVER Sending: ", reply)
    s.sendto(data, addr)
