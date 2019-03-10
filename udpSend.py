#http://www.ironpython.info/index.php?title=Sending_Udp_Packets

import socket
import time
import CarLampCallBack

def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.sendto(message, ("192.168.254.69", 5005))

send('6')
time.sleep(.3)
send("quit")

