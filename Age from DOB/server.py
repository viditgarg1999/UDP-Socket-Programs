import socket
from datetime import datetime
udp_ip="127.0.0.1"
udp_port=5006

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((udp_ip,udp_port))

while True:
    date,addr=s.recvfrom(1024)
    date=date.decode()

    day=int(date[0:2])
    month=int(date[3:5])
    year=int(date[6:])

    today=str(datetime.now())

    t_year=int(today[0:4])
    t_month=int(today[5:7])
    t_day=int(today[8:10])

    year_diff=t_year-year
    day_diff=t_day-day
    month_diff=t_month-month
    if((year_diff<=0 and month_diff<0)or(year_diff<=0 and month_diff<=0 and day_diff<0)):
        year_diff=year_diff-1;

    if(year_diff>=0):
        if(month_diff>=0):
            if(day_diff>=0):
                print("Years are:"+str(year_diff))
                print("Months are:"+str(month_diff))
                print("Days are:"+str(day_diff))
            elif(day_diff<0):
                #Taking month size as 30 for all the months
                month_diff=month_diff-1
                day_diff=day_diff+30;
                print("Years are:"+str(year_diff))
                print("Months are:"+str(month_diff))
                print("Days are:"+str(day_diff))
        elif(month_diff<0):
             if(day_diff>=0):
                year_diff=year_diff-1
                month_diff=month_diff+12
                print("Years are:"+str(year_diff))
                print("Months are:"+str(month_diff))
                print("Days are:"+str(day_diff))

             elif(day_diff<0):
                year_diff=year_diff-1
                month_diff=month_diff+12-1
                day_diff=day_diff+30
                print("Years are:"+str(year_diff))
                print("Months are:"+str(month_diff))
                print("Days are:"+str(day_diff))
        s.sendto(str(year_diff).encode(),addr)
        s.sendto(str(month_diff).encode(),addr)
        s.sendto(str(day_diff).encode(),addr)

    if(year_diff<0):
        print("Invalid DOB")
        s.sendto("Invalid DOB".encode(),addr)

    
        
