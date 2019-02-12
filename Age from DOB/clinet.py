import socket

udp_ip="127.0.0.1"
udp_port=5006

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((udp_ip,udp_port))

dob=input("Enter your Date of birth in dd-mm-yyyy:")
s.sendto(dob.encode(),(udp_ip,udp_port))

age,addr=s.recvfrom(1024)
print("Years are:"+str(age.decode()))

month,addr1=s.recvfrom(1024)
print("Months are:"+str(month.decode()))

days,addr2=s.recvfrom(1024)
print("Days are:"+str(days.decode()))
