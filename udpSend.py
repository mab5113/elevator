import socket
import time

def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(message.encode(), ("192.168.254.69", 5005))

floor = -99
while floor != 0:
	floor = input("Floor Number: ")
	send(str(floor))
# time.sleep(.3)
#send("quit")
