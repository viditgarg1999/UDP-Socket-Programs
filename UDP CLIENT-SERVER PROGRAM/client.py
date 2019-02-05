#SIMPLE UDP CLIENT SERVER PROGRAM

import socket

UDP_IP='127.0.0.1'
UDP_PORT=5005

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect((UDP_IP,UDP_PORT))

s.sendto('Hello Server'.encode(),((UDP_IP,UDP_PORT)))
