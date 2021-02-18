#!/usr/bin/python3
import socket
import time

rec_ip="127.0.0.1" #my ip ="192.168.10.197"
port=8881


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	x=input("enter the msg please::::::")
	s.sendto(x.encode(),(rec_ip,port))
	#time.sleep(1)
	s1=s.recvfrom(100)
	print(s1[0].decode())

