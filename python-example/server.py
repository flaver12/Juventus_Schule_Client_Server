import socket
import os
import re

ip = "127.0.0.1"

print("Enter port")
port = int(input())

print("========")
print("Runs on %s:%i (TCP)" % (ip, port))
print("========")

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((ip, port))
tcp.listen(1)

connect, address = tcp.accept()
print("Connection on", address)
connect.send(bytearray("hello world", 'utf8'))
connect.close()