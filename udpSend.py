import socket
import time
import json
def send(message, ip = "127.0.0.1"):
	port = 5005
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	#sock.sendto(message.encode(), (ip, port))
	sock.sendall(message, (ip, port))

c =1
msg='test'
while msg != "":
	
	# a Python object (dict):
	x = {
	  'name': 'John',
	  'age': 30,
	  'city': 'New York'
	}
	
	jsonObj = json.loads(x)

	send(jsonObj)
	c += 1
	time.sleep(1)
#send("quit")
