#!/usr/bin/python3

from HallButtonInitialize import HallButtonInitialize
from HallLampInitialize import HallLampInitialize
from udpListener import myListener

def HallManager(id):
	try:   	
		while True:
			time.sleep(.5)
			#print ('.')
			pass 
	except KeyboardInterrupt:
		# This will catch the ctrl-c to allow clean-up
		print ('Done,  exiting Hall Manager')
		# do cleanup here before shutting down
		pass 
