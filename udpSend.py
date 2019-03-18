import socket
# import time

def send(message, ip = "127.0.0.1"):
	port = 5005
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	sock.sendto(message.encode(), (ip, port))

c =1
while msg != "":
	send(c)
	c += 1
	time.sleep(1)
#send("quit")
