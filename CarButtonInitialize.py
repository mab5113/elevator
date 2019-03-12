#TODO: add description for this module
#  Use pin number from config.py as list and configure in loop

import time
import RPi.GPIO as GPIO
from CarLampCallBack import CarLampCallBack

def CarLampMonitor():

	# Use BCM GPIO references
	# instead of physical pin numbers
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
		
	GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

	GPIO.add_event_detect(14, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(15, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(16, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(17, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
	GPIO.add_event_detect(18, GPIO.RISING, callback=CarLampCallBack, bouncetime=400)  
