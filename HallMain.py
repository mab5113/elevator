
from HallButtonInitialize import HallButtonInitialize
from HallLampInitialize import HallLampInitialize

HallLampInitialize()
HallButtonInitialize()

try:   	
	while True:
		time.sleep(.5)
		#print ('.')
		pass 
except KeyboardInterrupt:
	# This will catch the ctrl-c to allow clean-up
	print ('Done')
	# do cleanup here
	pass 
