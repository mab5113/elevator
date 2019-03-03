#http://www.ironpython.info/index.php?title=Sending_Udp_Packets

import socket



def send(message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.sendto(message, ("192.168.254.70", 5010))


send("Some text")
