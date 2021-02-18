#!/usr/bin/python3
import socket
import matplotlib.pyplot as plt
import time


rec_ip="127.0.0.1" #rec_ip
my_port=8881   #5000+ port number will be free most of the time



#socket function in the socket library imported earlier

#we are using           ipv4,           UDP   
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
#for                  tcp       DGRAM  <-> STREAM

#binding ip and port
s.bind((rec_ip,my_port))

while True:
	data=s.recvfrom(100)
	rdata= " "+data[0].decode()+" "   #later the loop will find single word's existance in another words too.now it will find a word with a space
	print ("data from client,",rdata)
	#print "ip of client ,",data[1][0]
	#reply=input("enter your reply    :")
	#s.sendto(reply.encode(),data[1])
	lis=rdata.split()
	lis = list(set(lis))
	length=len(lis)
	for i in range(length):
		find = " "+str(lis[i]) + " "
		count=rdata.count(find,0,len(rdata))#list will contain words but string(rdata) will contain char with spaces
		time.sleep(2)
		plt.bar(i+1,count,label=str(lis[i]))
		#plt.scatter(i+1,count,label=str(lis[i]))
	plt.legend()
	plt.xlabel("words")
	plt.ylabel("count")	
	plt.show()
	
	
