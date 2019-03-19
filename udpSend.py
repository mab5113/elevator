import socket
import time
import json
import pickle


def send(message, ip = "10.81.104.104"):
	port = 5005
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	sock.sendto(message.encode(), (ip, port))
	#sock.sendall(message, (ip, port))

c =1
msg='test'
while msg != "":
	
	
	send('a,b,c')
	c += 1
	time.sleep(1)
#send("quit")
