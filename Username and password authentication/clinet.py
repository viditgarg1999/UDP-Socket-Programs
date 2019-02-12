import socket

UDP_IP='127.0.0.1'
UDP_PORT=5005

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((UDP_IP,UDP_PORT))

username=input('Enter username:')
password=input('Enter password:')

s.sendto(username.encode(),((UDP_IP,UDP_PORT)))
s.sendto(password.encode(),((UDP_IP,UDP_PORT)))

result,addr=s.recvfrom(1024)

print(result.decode())
