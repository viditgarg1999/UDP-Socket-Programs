import socket
import numpy

UDP_IP='127.0.0.1'
UDP_PORT=5005

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((UDP_IP,UDP_PORT))

#Available Datasets for Userid and Passwords:
a=[]
b=[]
a.append('admin')
b.append('admin')
a.append('vidit')
b.append('vidit')
a.append('tcp')
b.append('udp')

while True:
    username1,addr=s.recvfrom(1024)
    password1,addr=s.recvfrom(1024)

    username=username1.decode()
    password=password1.decode()
    k=0
    for i in range (3):
        if(password==b[i] and username==a[i]):
            print("Verified")
            s.sendto('Access Granted'.encode(),addr)
            break;
        else:
            k=k+1;
    if(k==3):
        print("Not Verified")
        s.sendto('Please Check your username and password'.encode(),addr)
    
    
