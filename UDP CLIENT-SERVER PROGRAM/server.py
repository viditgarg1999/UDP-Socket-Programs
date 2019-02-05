# SIMPLE UDP CLIENT SERVER PROGRAM

import socket

UDP_IP='127.0.0.1'
UDP_PORT=5005

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((UDP_IP,UDP_PORT))

while True:
    data,addr=s.recvfrom(1024)
    print('Data Given by user is:'+ str(data.decode()))
