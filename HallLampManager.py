# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

import time
import RPi.GPIO as GPIO
from HallLampCallBack import HallLampCallBack

def HallLampManager():

	print ('HallLampInitialize: initialize')
	# Use BCM GPIO references instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
		
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(14,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)

	GPIO.output(11,False)
	GPIO.output(12,False)
	GPIO.output(13,False)
	GPIO.output(14,False)
	GPIO.output(15,False)
	GPIO.output(16,False)
	GPIO.output(17,False)
	GPIO.output(18,False)
	time.sleep(2)
	GPIO.output(11,True)
	GPIO.output(12,True)
	GPIO.output(13,True)
	GPIO.output(14,True)
	GPIO.output(15,True)
	GPIO.output(16,True)
	GPIO.output(17,True)
	GPIO.output(18,True)

		
	GPIO.setup(3, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(4, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(5, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(6, GPIO.IN,  pull_up_down=GPIO.PUD_UP) 
	GPIO.setup(7, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(8, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(9, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

	GPIO.add_event_detect(3,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(4,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(5,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(6,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(7,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(8,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(9,  GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(10, GPIO.RISING, callback=HallLampCallBack, bouncetime=400)  

	try:   	
		while True:
			time.sleep(.5)
			#print ('.')
			pass # do the loop here
	except KeyboardInterrupt:
		# This will catch the ctrl-c to allow clean-up
		print ('Done')
		# do cleanup here
		pass 
		