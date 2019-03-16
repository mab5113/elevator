import socket
# import time

def send(ip, message):
	port = 5005
	if ip == '':
		ip = "192.168.254.69"
		
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	sock.sendto(message.encode(), (ip, port))

#floor = ""
#while floor != "-99":
#	floor = str(input("Floor Number: "))
#	send(floor)
# time.sleep(.3)
#send("quit")
