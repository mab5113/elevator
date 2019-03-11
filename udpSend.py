import socket
import time

def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.sendto(message, ("127.0.0.1", 5005))

send('6')
time.sleep(.3)
send("quit")
