import socket
import sys
import threading

class udp:

	print "Prepare client"
	UDP_IP = '0.0.0.0'  #accept connection on all ip address of the machine
	UDP_PORT = 1978 #accept connection only on port 1978
	BUFFER_SIZE = 1024 # we can receive at max 1024 bytes at time

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
	
	sock.bind((UDP_IP, UDP_PORT))
	
	def _sendUDP(msg):
	        while 1:
	                s.send(msg)
	def _readUDP():
	        while True:
		     data, addr = sock.recvfrom(1024) 		# buffer size is 1024 bytes
		     print "received message:", data



	writeth = threading.Thread(target=_sendUDP)
	writeth.start()
	
	readth = threading.Thread(target=_readUDP)
	readth.start()

