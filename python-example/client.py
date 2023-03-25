import socket
import os

ip = '127.0.0.1'
port = 4000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((ip, port))
load = "  " * 30
buffer = bytearray(load, 'uft8')
tcp.recv(buffer)
print(buffer)
tcp.close()