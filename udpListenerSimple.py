import config
import socket
import threading

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("Starting " + self.name)
		#threadlock.acquire()
		myListener()
		#threadlock.release()

	def stop(self):
		print ("udp listener thread exiting")
		exit()
    
def myListener():
#	UDP_IP = "192.168.254.69"
	UDP_IP = "0.0.0.0"		# Listen to all incoming datagrams
	UDP_PORT = 5005			# to this port
 
	sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP Datagram
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((UDP_IP, UDP_PORT))
 
	print ("starting udp listener")

	while True:
		msg, addr = sock.recvfrom(1024)	# buffer size is 1024 bytes
		msg = msg.decode('utf-8')
		print (msg)
		a,b,c = msg.split(',')
		print (a)
		print (b)
		print (c)
		if msg == 'quit':
			print ("Received quit message, exiting udp Listener")
			thread1.stop()
			pass
		#print (addr)


def Main(id):
	#threadlock = threading.Lock()
	thread1= myThread(1,"Thread1", 1)
	thread1.start()
	print ("udpListenerMain: udp listener thread started")
	myListener()

Main(1)
